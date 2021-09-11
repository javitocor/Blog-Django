from django.shortcuts import render, redirect
from .models import Blogger, Post, Tag, PostComment
from django.contrib.auth.decorators import login_required

# Create your views here.

def posts(request):
  pass

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

def registerView(request):
  pass