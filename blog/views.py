from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def posts_list(request):
    n = ['Name1', 'Name2', 'Name3']
    return render(request, 'blog/index.html', context={'names': n})