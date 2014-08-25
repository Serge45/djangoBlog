from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Blog post view')
# Create your views here.
