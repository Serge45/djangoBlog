from django.conf.urls import patterns, include, url

from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sergeBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls', namespace="blog")),
    url(r'', include('django.contrib.flatpages.urls')),
)

#urlpatterns += patterns(r'',
#                        settings.STATIC_URL, {'static' : settings.STATIC_ROOT})
#urlpatterns += patterns(r'',
#    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'static': settings.STATIC_ROOT}),
#)
