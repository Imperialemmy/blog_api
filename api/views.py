from tkinter import Image

from rest_framework.response import Response
from .filters import PostFilter
from .serializers import UserSerializer,CategorySerializer,CommentSerializer,PostSerializer,TagSerializer,ImageSerializer
from blog.models import Post, Category, Comment, User, Tag,PostImage
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.


class APIPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter,OrderingFilter)
    # filterset_fields = ('category','tags',)
    filterset_class = PostFilter # Custom filtering
    search_fields = ['title']
    ordering_fields = ['title','created_at']
    pagination_class = PageNumberPagination


class APIUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        username = request.data['username']
        bio = request.data['bio']
        profile_image = request.data['profile_image']

        User.objects.create(username=username, bio=bio, profile_image=profile_image)

        return Response("User created successfully")

    def update(self, request, *args, **kwargs):
        # Get the current user object using the pk from the URL
        instance = self.get_object()
        # You can validate and update the object here if needed
        serializer = self.get_serializer(instance, data=request.data, partial=True)  # `partial=True` allows updating only certain fields
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("User updated successfully")

class APICommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend,OrderingFilter)
    ordering_fields = ['created_at']

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk'])# filtering the comments based on the post

    def get_serializer_context(self):
        return {'post_id':self.kwargs['post_pk']}# returning the post_id value as the primary key


class APITagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class APICategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class APIImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer

    def get_queryset(self):
        return PostImage.objects.filter(post_id=self.kwargs['post_pk'])

    def get_serializer_context(self):
        return {'post_id': self.kwargs['post_pk']}











