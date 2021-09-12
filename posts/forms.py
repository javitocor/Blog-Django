from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ckeditor.widgets import CKEditorWidget

from .models import *

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ['author', 'created']
  def __init__(self, *args, **kwargs):
    super(PostForm, self).__init__(*args, **kwargs)
    self.fields['headline'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter headline'})
    self.fields['sub_headline'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter sub headline'})
    self.fields['tags'].widget.attrs.update({'class':'form-control w-25 mb-3'})
    self.fields['thumbnail'].widget.attrs.update({'class':'form-control'})
    self.fields['body'].widget.attrs.update({'class':'form-control'})

class PostCommentForm(forms.ModelForm):
  class Meta:
    model = PostComment
    exclude = ['author', 'post']

class BloggerForm(forms.ModelForm):
  class Meta:
    model = Blogger
    exclude = ['user', 'joined']
  def __init__(self, *args, **kwargs):
    super(BloggerForm, self).__init__(*args, **kwargs)
    self.fields['first_name'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter first name'})
    self.fields['last_name'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter last name'})
    self.fields['email'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter email'})
    self.fields['avatar'].widget.attrs.update({'class':'form-control'})
    self.fields['bio'].widget.attrs.update({'class':'form-control'})
    self.fields['twitter'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter twitter account'})

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