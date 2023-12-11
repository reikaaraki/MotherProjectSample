from django import forms
from .models import Post, Comment

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title','content',
        )
        widgets = {
            'title': forms.Textarea(
                attrs={'rows': 5, 'cols': 30,
                       'placeholder': 'ここに入力してください'}
            ),
        }
        widgets = {
            'content': forms.Textarea(
                attrs={'rows': 5, 'cols': 30,
                       'placeholder': 'ここに入力してください'}
            ),
        }

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'content',
        )        
        widgets = {
            'content': forms.Textarea(
                attrs={'rows': 5, 'cols': 30}
            ),
        }

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'text',
        )    
        widgets = {
            'text': forms.Textarea(
                attrs={'rows': 5, 'cols': 30}
            ),
        } 
        labels = {
            'text': '本文',
        }   
            