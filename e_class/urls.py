<<<<<<< HEAD
from django.urls import path, include #type:ignore
from .views import UserViewSet
from rest_framework.routers import DefaultRouter #type:ignore

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
=======
from django.urls import path
from .views import index

urlpatterns = [
    path('e_class/', index),
]
>>>>>>> main
