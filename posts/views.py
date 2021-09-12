from django.shortcuts import render, redirect
from .models import Blogger, Post, Tag, PostComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, PostForm, PostCommentForm, BloggerForm, UserForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import PostFilter

# Create your views here.

def posts(request):
    posts = Post.objects.order_by('-created')
    filter = PostFilter(request.GET, queryset=posts)
    posts = filter.qs
    tags = Tag.objects.all()

    page = request.GET.get('page')

    paginator = Paginator(posts, 5)

    try:
      posts = paginator.page(page)
    except PageNotAnInteger:
      posts = paginator.page(1)
    except EmptyPage:
      posts = paginator.page(paginator.num_pages)

    context = {
      'posts': posts,
      'tags':tags,
      'filter': filter,
    }
    return render(request, 'posts/posts.html', context)

@login_required(login_url='login')
def postDetail(request, pk):

  tags = Tag.objects.all()
  post = Post.objects.get(pk=pk)
  selftags = post.tags.all()

  if request.method == 'POST':
		  PostComment.objects.create(
        author=request.user.blogger,
        post=post,
        body=request.POST['comment']
        )

		  return redirect('post-detail', pk=pk)

  context = {
    'post': post,
    'tags': tags,
    'selftags':selftags
  }
  return render(request, 'posts/post_detail.html', context)

@login_required(login_url='login')
def postCreate(request):
    form = PostForm()

    if request.method == 'POST':
      form = PostForm(request.POST, request.FILES)
      if form.is_valid():
        obj = form.save(commit=False)
        obj.author = Blogger.objects.get(user=request.user)
        obj.save()
        obj.tags.add(request.POST['tags'])
      return redirect('post-detail', pk=obj.pk)

    context = {'form':form}
    return render(request, 'posts/post_form.html', context)

@login_required(login_url='login')
def postUpdate(request, pk):
  post = Post.objects.get(pk=pk)
  form = PostForm(instance=post)

  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
      form.save()
    return redirect('post-detail', pk=post.pk)

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

  page = request.GET.get('page')

  paginator = Paginator(bloggers, 5)

  try:
    bloggers = paginator.page(page)
  except PageNotAnInteger:
    bloggers = paginator.page(1)
  except EmptyPage:
    bloggers = paginator.page(paginator.num_pages)

  context = {'bloggers':bloggers}
  return render(request, 'posts/bloggers.html', context)

@login_required(login_url='login')
def bloggerDetail(request, pk):
  blogger = Blogger.objects.get(user_id=pk)
  blogger_posts = blogger.post_set.all()
  context = {'blogger':blogger, 'posts': blogger_posts}
  return render(request, 'posts/blogger_detail.html', context)

@login_required(login_url='login')
def bloggerUpdate(request):
  user = request.user
  blogger = user.blogger
  form = BloggerForm(instance=blogger)

  if request.method == 'POST':
      user_form = UserForm(request.POST, instance=user)
      if user_form.is_valid():
        user_form.save()

      form = BloggerForm(request.POST, request.FILES, instance=blogger,)
      if form.is_valid():
        form.save()
      return redirect('blogger-detail', pk=blogger.pk)

  context = {'form':form}
  return render(request, 'posts/blogger_form.html', context)

@login_required(login_url='login')
def bloggerDelete(request, pk):
  blogger = Blogger.objects.get(pk=pk)
  if request.method == 'POST':
		  blogger.delete()
		  return redirect('signup')
  context = {'item':blogger}
  return render(request, 'posts/delete.html', context)

def registerView(request):
  form  = CustomUserCreationForm()

  if request.method == 'POST':
    form  = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.save()

      user = authenticate(request, username=user.username, password=request.POST['password1'])

      if user is not None:
        login(request, user)
        return redirect('posts')

  context = {
    'form': form,
  }
  return render(request, 'posts/signup.html', context)