from django.contrib import admin
from .models import Post
from .models import Message

# Register your models here.

admin.site.register(Post)
admin.site.register(Message)