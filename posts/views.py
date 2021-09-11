from django.shortcuts import render, redirect
from .models import Blogger, Post, Tag, PostComment
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

# Create your views here.

def posts(request):
  return render(request, 'posts/posts.html')

@login_required(login_url='login')
def postDetail(request, pk):
  pass

@login_required(login_url='login')
def postCreate(request):
  pass

@login_required(login_url='login')
def postUpdate(request, pk):
  pass

@login_required(login_url='login')
def postDelete(request, pk):
  pass

@login_required(login_url='login')
def bloggers(request):
  pass

@login_required(login_url='login')
def bloggerDetail(request, pk):
  pass

@login_required(login_url='login')
def bloggerUpdate(request, pk):
  pass

@login_required(login_url='login')
def bloggerDelete(request, pk):
  pass

def registerView(request):
  return render(request, 'posts/signup.html')