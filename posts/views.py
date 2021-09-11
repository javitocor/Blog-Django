from django.shortcuts import render, redirect
from .models import Blogger, Post, Tag, PostComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, PostForm, PostCommentForm, BloggerForm

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
  tags = Tag.objects.all()
  post = Post.objects.get(pk=pk)

  context = {
    'post': post,
    'tags': tags,
  }
  return render(request, 'posts/post_detail.html', context)

@login_required(login_url='login')
def postCreate(request):
    form = PostForm()

    if request.method == 'POST':
      form = PostForm(request.POST)
      if form.is_valid():
        form.save()
      return redirect('posts')

    context = {'form':form}
    return render(request, 'posts/post_form.html', context)

@login_required(login_url='login')
def postUpdate(request, pk):
  post = Post.objects.get(pk=pk)
  form = PostForm(instance=post)

  if request.method == 'POST':
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
      form.save()
    return redirect('posts')

  context = {'form':form}
  return render(request, 'posts/post_form.html', context)

@login_required(login_url='login')
def postDelete(request, pk):
  post = Post.objects.get(pk=pk)
  if request.method == 'POST':
		  post.delete()
		  return redirect('posts')
  context = {'item':post}
  return render(request, 'posts/delete.html', context)

@login_required(login_url='login')
def bloggers(request):
  bloggers = Blogger.objects.all()

  context = {'bloggers':bloggers}
  return render(request, 'posts/bloggers.html', context)

@login_required(login_url='login')
def bloggerDetail(request, pk):
  blogger = Blogger.objects.get(pk=pk)

  context = {'blogger':blogger}
  return render(request, 'posts/blogger_detail.html', context)

@login_required(login_url='login')
def bloggerUpdate(request, pk):
  blogger = Blogger.objects.get(pk=pk)
  form = BloggerForm(instance=blogger)

  if request.method == 'POST':
    form = BloggerForm(request.POST, instance=blogger)
    if form.is_valid():
      form.save()
    return redirect('posts')

  context = {'form':form}
  return render(request, 'posts/blogger_form.html', context)

@login_required(login_url='login')
def bloggerDelete(request, pk):
  blogger = Blogger.objects.get(pk=pk)
  if request.method == 'POST':
		  blogger.delete()
		  return redirect('posts')
  context = {'item':blogger}
  return render(request, 'posts/delete.html', context)

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