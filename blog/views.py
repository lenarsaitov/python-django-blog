from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
# Create your views here.

def posts_list(request):
    post = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': post})

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact = slug)
    return render(request, 'blog/post_detail.html', context={'post': post})