from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post, Tag
from django.views.generic import View
from .utils import ObjectDetailMixin
from django.http import HttpResponse
from blog.forms import TagForm

# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'

def tags_lists(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags':tags})

class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form':form})

    # def post(self, request):