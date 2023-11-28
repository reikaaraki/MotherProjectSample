from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from .forms import RegistForm,UserLoginForm, ProfileForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User, Relationship

class HomeView(TemplateView):
   template_name = 'accounts/home.html'

class RegistUserView(CreateView):
   template_name = 'accounts/regist.html'
   form_class = RegistForm

   def form_valid(self, form):
      password = form.cleaned_data['password1']

      return super().form_valid(form)
   
class UserLoginView(LoginView): 
   template_name = 'accounts/login.html'
   authentication_form = UserLoginForm  

class UserLogoutView(LogoutView):
   pass   

class ProfileEditView(LoginRequiredMixin, UpdateView):
   template_name = 'accounts/edit_profile.html'
   model = User
   form_class = ProfileForm
   success_url = '/accounts/edit_profile/'
   def get_object(self):
      return self.request.user
   
class UserListView(LoginRequiredMixin, ListView):
   template_name = 'accounts/userlist.html'
   model = User

   def get_queryset(self):
      return User.objects.all()   
   
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      user = self.request.user
      followings = (Relationship.objects.filter(follower_id=user.pk)).values_list('following_id')
      context['following_list'] = User.objects.filter(id__in=followings)
      return context   
   
def mk_relation(request, pk):
   follower = get_object_or_404(User,pk=request.user.pk)
   following = get_object_or_404(User, pk=pk)
   make_relation = Relationship(follower_id=follower.pk, following_id=following.pk)
   make_relation.save()
   return redirect('accounts:userlist')

def rm_relation(request, pk):
   follower = get_object_or_404(User, pk=request.user.pk)
   following = get_object_or_404(User, pk=pk)
   clear_relation = Relationship.objects.filter(follower_id=follower.pk, following_id=following.pk)
   clear_relation.delete()
   return redirect('accounts:userlist')