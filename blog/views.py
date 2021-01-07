from django.shortcuts import render
from django.shortcuts import redirect
from .models import Post, Tag
from django.views.generic import View
from .utils import *
from blog.forms import TagForm, PostForm

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'

class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create.html'

class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'


class TagDetail(ObjectDetailMixin, View):
    form_model = Tag
    template = 'blog/tag_detail.html'

def tags_lists(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags':tags})

class TagCreate(ObjectCreateMixin, View):
    model = TagForm
    template = 'blog/tag_create.html'

class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'
