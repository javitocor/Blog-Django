from django.db import models
from django.contrib.auth.models import User
import datetime

YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]


class Blogger(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200)
    #avatar = models.ImageField(null=True, blank=True, upload_to="images", default="/user.png")
    bio = models.TextField(null=True, blank=True)
    joined = models.IntegerField(default=datetime.datetime.now().year)
    twitter = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
      name = str(self.first_name)
      if self.last_name:
        name += ' ' + str(self.last_name)
      return name

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
      return self.name

class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    #thumbnail = models.ImageField(null=True, blank=True, upload_to="images", default="/images/placeholder.png")
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
      return self.headline


class PostComment(models.Model):
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
      return self.body
