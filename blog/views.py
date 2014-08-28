from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Category, BlogPost, Tag

class CategoryListView(ListView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            category = Category.objects.get(slug=slug)
            return BlogPost.objects.filter(category=category)
        except Category.DoesNotExist:
            return BlogPost.objects.none()

class TagListView(ListView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            tag = Tag.objects.get(slug=slug)
            return tag.blogpost_set.all()
        except Tag.DoesNotExist:
            return BlogPost.objects.none()
