from django.contrib import admin
from blog.models import BlogPost
import models

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'post_datetime', 'last_update_datetime', 'user')
    search_fields = ['title']
    prepopulated_fields = {"slug" : ("title", ), }

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(models.Category)
admin.site.register(BlogPost, BlogPostAdmin)
# Register your models here.
