from django.contrib import admin
from .models import User, Post, Category, Comment, Tag,PostImage
# Register your models here.

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(PostImage)
