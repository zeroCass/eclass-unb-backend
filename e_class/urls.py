from django.urls import path, include #type:ignore
from .views import *
from rest_framework.routers import DefaultRouter #type:ignore

router = DefaultRouter()
router.register('students', StudentsViewSet, basename='students')
router.register('teachers', TeachersViewSet, basename='teachers')
router.register('admins', AdminsViewSet, basename='admins')
router.register('subjects', SubjectsViewSet, basename='subjects')
router.register('classes', ClassesViewSet, basename='classes')
router.register('questions', QuestionViewSet, basename='questions')
router.register('multiple-questions', MultipleQuestionViewSet, basename='multiple-questions')
router.register('discursive-questions', DiscursiveQuestionViewSet, basename='discursive-questions')
router.register('exams', ExamsViewSet, basename='exams')

urlpatterns = [
    path('', include(router.urls)),
]
