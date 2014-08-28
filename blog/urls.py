from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from blog.views import CategoryListView, TagListView
from blog.models import BlogPost, Category, Tag

urlpatterns = patterns('',
                       #url(r'^$', ListView.as_view(model=BlogPost)),
                       #Index
                       url(r'^(?P<page>\d+)?/?$', ListView.as_view(model=BlogPost, paginate_by=5, )),
                       #Detail views
                       url(r'^(?P<post_datetime__year>\d{4})/(?P<post_datetime__month>\d{1,2})/(?P<slug>[a-zA-Z0-9-]+)/?$',
                           DetailView.as_view(model=BlogPost)),
                       #Categories
                       url(r'^category/(?P<slug>[a-zA-Z0-9-]+)/?$', CategoryListView.as_view(
                           paginate_by=5,
                           model=Category,
                       )),
                       url(r'^tag/(?P<slug>[a-zA-Z0-9-]+)/?$', TagListView.as_view(
                           paginate_by=5,
                           model=Tag,
                       )),
)