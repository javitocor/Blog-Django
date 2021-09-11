from django.shortcuts import render, redirect
from .models import Blogger, Post, Tag, PostComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm

# Create your views here.

def posts(request):
  posts = Post.objects.all()
  tags = Tag.objects.all()

  context = {
    'posts': posts,
    'tags':tags,
  }
  return render(request, 'posts/posts.html', context)

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
  form  = CustomUserCreationForm()

  if request.method == 'POST':
    form  = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.save()
      blogger = Blogger.objects.create(user=user)

      user = authenticate(request, username=user.username, password=request.POST['password1'])

      if user is not None:
        login(request, user)
        return redirect('posts')

  context = {
    'form': form,
  }
  return render(request, 'posts/signup.html', context)