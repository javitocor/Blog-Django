from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import *

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ['author']

  widgets = {
			'tags':forms.CheckboxSelectMultiple,
		}

class PostCommentForm(forms.ModelForm):
  class Meta:
    model = PostComment
    exclude = ['author', 'post']

class BloggerForm(forms.ModelForm):
  class Meta:
    model = Blogger
    exclude = ['user', 'joined']


class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'password1', 'password2']
    
  def __init__(self, *args, **kwargs):
    super(CustomUserCreationForm, self).__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter username'})
    self.fields['password1'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter password'})
    self.fields['password2'].widget.attrs.update({'class':'form-control', 'placeholder':'Confirm password'})

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']