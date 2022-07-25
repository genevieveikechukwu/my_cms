from email import message
from unicodedata import name
from django.db import models

# Create your models here.


class template(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=300)
    description = models.TextField()
    created_At = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class user(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    template = models.ForeignKey(template, on_delete=models.CASCADE, null=True)


    def __str__(self) -> str:
        return self.username


class setting(models.Model):
     user = models.ManyToManyField(user)
     name = models.CharField(max_length=250)
     value = models.CharField(max_length=200)
     autoload = models.BooleanField(default=True)


class page(models.Model):
    Template_name = models.ForeignKey(template, on_delete=models.CASCADE, related_name='template_pages')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300)
    created_At = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name



class page_field(models.Model):
    page_created_from = models.ManyToManyField(page)
    name = models.CharField(max_length=20)
    description = models.TextField()
    created_At = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


