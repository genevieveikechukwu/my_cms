from django.contrib import admin

from .models import Post, Comment, Profile, Category

# Register your models here.

admin.site.register (Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    # readonly_fields = ["slug"]
    prepopulated_fields = {'slug': ('title',)}
    
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # list_display = ('name', 'email', 'post', 'created', 'active')
    list_display = ('user','post', 'created', 'active' )
    list_filter = ('active', 'created', 'updated')
    # search_fields = ('name', 'email', 'body')
    search_fields = ('user', 'body')
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']