from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from django.contrib.sitemaps.views import sitemap
from blog.sitemap import BlogPostSitemap, FlatPageSitemap
from blog.views import CategoryListView, TagListView, PostsFeed
from blog.models import BlogPost, Category, Tag

sitemaps = {
    'post' : BlogPostSitemap,
    'pages': FlatPageSitemap
}

urlpatterns = patterns('',
                       #Index
                       url(r'^(?P<page>\d+)?/?$',
                           ListView.as_view(model=BlogPost, paginate_by=5),
                           name="index"),
                       #Detail views
                       url(r'^(?P<post_datetime__year>\d{4})/(?P<post_datetime__month>\d{1,2})/(?P<slug>[a-zA-Z0-9-]+)/?$',
                           DetailView.as_view(model=BlogPost),
                           name="post"),
                       #Categories
                       url(r'^category/(?P<slug>[a-zA-Z0-9-]+)/?$',
                           CategoryListView.as_view(paginate_by=5,
                                                    model=Category),
                           name="category"
                       ),
                       #Tags
                       url(r'^tag/(?P<slug>[a-zA-Z0-9-]+)/?$',
                           TagListView.as_view(paginate_by=5,
                                               model=Tag),
                           name="tag"
                       ),
                       #Post RSS feed
                       url(r'^feeds/posts/$', PostsFeed()),
                       #Search result
                       url(r'^search', 'blog.views.get_search_result', name="search"),

                       #Sitemap
                       url(r'^sitemap\.xml', sitemap, {'sitemap': sitemaps} ,
                                                       name='django.contrib.sitemaps.views.sitemap'),
)

