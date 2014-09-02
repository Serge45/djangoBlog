from django.contrib.sitemaps import Sitemap
from django.contrib.flatpages.models import FlatPage
from blog.models import BlogPost

class BlogPostSitemap(Sitemap):
    change_freq = "always"
    priority = 0.5

    def items(self):
        return BlogPost.objects.all()

    def last_modification(self, obj):
        return obj.last_update_datetime

class FlatPageSitemap(Sitemap):
    change_freq = "always"
    priority = 0.5

    def items(self):
        return FlatPage.objects.all()