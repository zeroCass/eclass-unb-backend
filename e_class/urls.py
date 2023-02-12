from django.urls import path, include #type:ignore
from .views.view_students import *
from .views.view_teachers import *
from .views.view_admins import *
from .views.view_auth import *
from .views.view_subjects import *
from .views.view_classes import *
from .views.view_multipleQuestions import *
from .views.views_discursiveQuestions import *
# from rest_framework.routers import DefaultRouter #type:ignore

urlpatterns = [
    path('students/', studentsList.as_view()),
    path('student/<int:pk>/', studentOne.as_view()),
    path('teachers/', teachersList.as_view()),
    path('teacher/<int:pk>/', teacherOne.as_view()),
    path('admins/', adminsList.as_view()),
    path('admin/<int:pk>/', adminOne.as_view()),
    path('login/', login.as_view()),
    path('logout/', logout.as_view()),
    path('subjects/', subjectsList.as_view()),
    path('subject/<int:pk>/', subjectsOne.as_view()),
    path('classes/', classesList.as_view()),
    path('class/<int:pk>/', classesOne.as_view()),
    path('multiple-questions/', multipleQuestionsList.as_view()),
    path('multiple-question/<int:pk>/', multipleQuestionsOne.as_view()),
    path('discursive-questions/', discursiveQuestionsList.as_view()),
    path('discursive-question/<int:pk>/', discursiveQuestionsOne.as_view()),
]
