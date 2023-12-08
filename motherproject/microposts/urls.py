from django.urls import path
from .views import (
    PostCreateView, PostListView, PostUpdateView, PostDeleteView, MyPostsView,
    FollowersView, FollowingView, PostDetailView, CommentCreateView,
)
from . import views
app_name = 'microposts'
urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create'),
    path('postlist/', PostListView.as_view(), name='postlist'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
    path('myposts/', MyPostsView.as_view(), name='myposts'),
    path('follower/', FollowersView.as_view(), name='follower'),
    path('following/', FollowingView.as_view(), name='following'),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('comment/create/<int:pk>/', CommentCreateView.as_view(), name='comment_create'),
]