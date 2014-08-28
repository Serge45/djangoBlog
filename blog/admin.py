from django.contrib import admin
import models

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'post_datetime', 'last_update_datetime', 'user')
    search_fields = ['title']
    prepopulated_fields = {"slug" : ("title", ), }

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.BlogPost, BlogPostAdmin)
# Register your models here.
