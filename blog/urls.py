from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name = 'posts_list_url'),
    path('post/create', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(model=Post), name='post_detail_url'),
    path('tags/', tags_lists, name = 'tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(model=Tag), name='tag_detail_url'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url')
]