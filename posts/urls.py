from django.urls import path

from . import views

urlpatterns = [
    path('', views.posts, name="posts"),
    path('post_detail/<int:pk>', views.postDetail , name="post-detail"),
    path('post/create', views.postCreate, name="post-create"),
    path('post/<int:pk>/update', views.postUpdate, name="post-update"),
    path('post/<int:pk>/delete', views.postDelete, name="post-delete"),
    path('bloggers/', views.bloggers , name="bloggers"),
    path('blogger_detail/<int:pk>', views.bloggerDetail, name="blogger-detail"),
    path('blogger/update', views.bloggerUpdate, name="blogger-update"),
    path('blogger/<int:pk>/delete', views.bloggerDelete, name="blogger-delete"),
    path('accounts/signup', views.registerView, name='signup'),
]