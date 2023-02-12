from rest_framework import viewsets # type: ignore
from .models import *
from .serializer import *

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer

class TeachersViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeachersSerializer

class AdminsViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminsSerializer

class SubjectsViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectsSerializer

class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

class MultipleQuestionViewSet(viewsets.ModelViewSet):
    queryset = MultipleQuestion.objects.all()
    serializer_class = MultipleQuestionSerializer

class DiscursiveQuestionViewSet(viewsets.ModelViewSet):
    queryset = DiscursiveQuestion.objects.all()
    serializer_class = DiscursiveQuestionSerializer

class ExamsViewSet(viewsets.ModelViewSet):
    queryset = Exams.objects.all()
    serializer_class = ExamsSerializer
