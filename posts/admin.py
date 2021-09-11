from django.contrib import admin
from .models import Blogger, Post, Tag, PostComment

# Register your models here.
admin.site.register(Tag)
admin.site.register(Blogger)
admin.site.register(Post)
admin.site.register(PostComment)
