from django.urls import path, include #type:ignore
from .views.view_students import *
# from rest_framework.routers import DefaultRouter #type:ignore

urlpatterns = [
    path('students/', studentsList.as_view()),
    path('students/<int:pk>/', studentOne.as_view()),
]
