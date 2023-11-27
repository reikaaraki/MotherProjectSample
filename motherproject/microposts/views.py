from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostCreateForm, PostUpdateForm
from django.contrib import messages
from django.urls import reverse_lazy
from accounts.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'microposts/create.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('microposts:create')

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.pk
        messages.success(self.request, '投稿が完了しました')
        return super(PostCreateView, self).form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, '投稿が失敗しました')
        return redirect('microposts:create')
    
class PostListView(LoginRequiredMixin, ListView):
    template_name = 'microposts/postlist.html'
    model = Post
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['favourite_list'] = user.favourite_post.all()

        return context

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'microposts/update.html'

    def form_valid(self, form):
        messages.success(self.request, '更新が完了しました')   
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('microposts:update', kwargs={'pk': self.kwargs['pk']})

    def form_invalid(self, form):
        messages.warning(self.request, '更新が失敗しました')
        return super().form_invalid(form)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'microposts/delete.html'

    success_url = reverse_lazy('microposts:myposts')
    success_message = "投稿は削除されました"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostDeleteView, self).delete(request, *args, **kwargs)
    
class MyPostsView(LoginRequiredMixin, ListView):
    template_name = 'microposts/myposts.html'
    model = Post
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(owner_id=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        qs = Post.objects.filter(owner_id=self.request.user)
        context['my_posts_count'] = qs.count()
        return context
    
