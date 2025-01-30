from django.urls import include, path
from .views import APIPostViewSet, APICommentViewSet, APIUserViewSet, APITagViewSet,APICategoryViewSet,APIImageViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()

router.register('posts',APIPostViewSet,basename='posts')
# router.register('posts/comments/<int:pk>', APICommentViewSet, basename='comment')
router.register('users', APIUserViewSet, basename='users')
router.register('tags', APITagViewSet, basename='tags')
router.register('categories', APICategoryViewSet, basename='categories')

post_comments_router = routers.NestedDefaultRouter(router, 'posts', lookup='post')
post_images_router = routers.NestedDefaultRouter(router, 'posts', lookup='post')

post_comments_router.register('comments', APICommentViewSet, basename='comments')

post_images_router.register('images', APIImageViewSet, basename='images')

# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)), # Main API
    path('', include(post_comments_router.urls)), # Comments API
    path('', include(post_images_router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)