from uuid import uuid4
from ckeditor.fields import RichTextField

from django.conf import settings
from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from matplotlib.image import thumbnail



from .managers import PublishedManager

# Create your models here.

User = settings.AUTH_USER_MODEL

class Category(models.Model):
    name  = models.CharField(max_length=255)
    
    
    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    
    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = "post_category")
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True, null=True , unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    thumbnail = models.ImageField(blank=True, null=True, upload_to="blog")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    
    class Meta:
        ordering = ['-publish']
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

        
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user")
    # name = models.CharField(max_length=80)
    # email = models.EmailField()
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('created',)
        
    def __str__(self):
        return f'Comment by {self.user} on {self.post}'



class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=25)
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    @admin.display(ordering="user__first_name")
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering="user__last_name")
    def last_name(self):
        return self.user.last_name

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        ordering = ["user__first_name", "user__last_name"]
        # permissions = [("view_history", "Can view history")]

    