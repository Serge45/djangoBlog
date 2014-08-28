from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Category, BlogPost

class CategoryListView(ListView):
    def get_queryset(self):
        slug = self.page_kwarg['slug']
        try:
            category = Category.objects.get(slug=slug)
            return BlogPost.objects.filter(category=category)
        except Category.DoesNotExist:
            return BlogPost.objects.none()

