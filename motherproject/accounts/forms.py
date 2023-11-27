from django import forms
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm


class RegistForm(forms.ModelForm):
    username = forms.CharField(label='ユーザーネーム')
    email = forms.EmailField(label='メールアドレス')
    password1 = forms.CharField(label='パスワード',widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード（確認用）',widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'confirm_password']

    def save(self, commit=False):
        user = super().save(commit=False)
        password = self.cleaned_data['password1']
        validate_password(password, user)
        user.set_password(password)
        user.save()
        return user    
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("パスワードが一致しません")
        
        return cleaned_data
    
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='ユーザーネーム')
    password = forms.CharField(label='パスワード',widget=forms.PasswordInput)

class ProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'age', 'avatar')
        help_texts = {
            'username': None,
            'email': None,
        }     

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
           