from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.syndication.views import Feed
from blog.models import Category, BlogPost, Tag

class PostsFeed(Feed):
    title = "RSS feed - posts"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return BlogPost.objects.order_by('-post_datetime')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

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
