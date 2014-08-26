from django.contrib import admin
from blog.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'post_datetime', 'last_update_datetime', 'user')
    search_fields = ['title']

admin.site.register(BlogPost, BlogPostAdmin)
# Register your models here.
