from django.urls import path, include #type:ignore
from .views import *
from rest_framework.routers import DefaultRouter #type:ignore

router = DefaultRouter()
router.register('students', StudentsViewSet, basename='students')
router.register('teachers', TeachersViewSet, basename='teachers')

urlpatterns = [
    path('', include(router.urls)),
]
