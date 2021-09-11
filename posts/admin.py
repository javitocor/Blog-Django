from django.contrib import admin
from .models import Blogger, Post, Task, PostComment

# Register your models here.
admin.site.register(Task)
admin.site.register(Blogger)
admin.site.register(Post)
admin.site.register(PostComment)
