from rest_framework import serializers
from blog.models import User, Post, Category, Comment, Tag, PostImage


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = PostImage
        fields = ['id', 'image', 'caption']



class UserSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(required=False, use_url=True, allow_null=True)
    class Meta:
        model = User
        fields = ['id','username','bio','profile_image']


class PostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    tags = serializers.SlugRelatedField(slug_field='name', many=True, queryset=Tag.objects.all())
    images = ImageSerializer(many=True, read_only=True)  # Read-only images field
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=100, allow_empty_file=False, use_url=False),
        write_only=True, required=False
    )

    class Meta:
        model = Post
        fields = ['id','title', 'content', 'images', 'category', 'author', 'tags', 'uploaded_images', 'created_at', 'updated_at']
        read_only_fields = ('created_at', 'updated_at')

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])  # Correct field name
        tags = validated_data.pop('tags', [])
        post = Post.objects.create(**validated_data)
        post.tags.set(tags)  # ✅ Correct way to assign ManyToManyField
        # Save images to the PostImage model
        for image in uploaded_images:
            PostImage.objects.create(post=post, image=image)  # Create image instance

        return post



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','description','created_at']
        read_only_fields = ['created_at']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    post = serializers.SlugRelatedField(slug_field='title', queryset=Post.objects.all())
    class Meta:
        model = Comment
        fields = ['comment','created_at','author','post']
        read_only_fields = ['created_at']

    def create(self, validated_data):
        post_id = self.context['post_id']# getting the id of the post
        Comment.objects.create(post_id=post_id, **validated_data)# creating an object under the post


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']



