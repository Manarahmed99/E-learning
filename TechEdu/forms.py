
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.utils.translation import gettext_lazy as _

from django.forms import TextInput, EmailInput , PasswordInput

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import TextInput, EmailInput



class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='اسم المستخدم', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    

    class Meta:
        model=User
        fields={'username','password'}






class CreateUserForm(UserCreationForm):
    username = forms.CharField(label='اسم المستخدم',widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='الايميل',widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='كلمة المرور',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='تاكيد كلمة المرور',widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')






