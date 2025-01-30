#make your custom filters here

from django_filters.rest_framework import FilterSet
from rest_framework.filters import SearchFilter
from unicodedata import category

from blog.models import Post

class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'category':['exact'],
            'tags':['exact'],
        }