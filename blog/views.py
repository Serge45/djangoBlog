from django.shortcuts import render, get_object_or_404
from blog.models import BlogPost

def index(request):
    blog_post_list = BlogPost.objects.all()
    context = {'blog/blogpost_list.html' : blog_post_list}
    return render(request, 'blog/blogpost_list.html', context)

def blog_content(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blog/post_content.html', {'post' : post,})
