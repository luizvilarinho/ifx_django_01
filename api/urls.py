from django.urls import path, include
from .views import BookViewSet, ModelViewSet, CourseViewSet, collectionViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('books', BookViewSet, basename='Books')
router.register('models', ModelViewSet, basename='Model')
router.register('courses', CourseViewSet, basename='Course')
#router.register('collection', collection, basename='Collection')


urlpatterns = [
    path('', include(router.urls)),
    path('collection/', collectionViewSet)
]