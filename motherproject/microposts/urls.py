from django.urls import path
from .views import (
    PostCreateView, PostListView, PostUpdateView, PostDeleteView, MyPostsView,
    FollowersView,FollowingView,
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
]