from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.views.generic import ListView
from django.contrib.syndication.views import Feed
from blog.models import Category, BlogPost, Tag
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
import markdown2

class PostsFeed(Feed):
    title = "RSS feed - posts"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return BlogPost.objects.order_by('-post_datetime')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        extras = ["fenced-code-blocks"]
        content = mark_safe(markdown2.markdown(force_unicode(item.content), extras))
        return content

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

def get_search_result(request):
    """
        Search for a post by title or content
        """
    query = request.GET.get('q', '')
    page = request.GET.get('page', 1)

    if query:
        results = BlogPost.objects.filter(Q(content__icontains=query) | Q(title__icontains=query))
    else:
        results = []

    pages = Paginator(results, 5)

    try:
        returned_page = pages.page(page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)

    return render_to_response('blog/search_post_list.html',
                              {'page_obj' : returned_page,
                               'object_list' : returned_page.object_list,
                               'search' : query})
