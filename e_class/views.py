#from django.shortcuts import render
#from django.http import HttpResponse
from rest_framework import viewsets # type: ignore
from .models import *
from .serializer import *
#from random import randint
#from rest_framework.authentication import TokenAuthentication
#from rest_framework.authtoken.views import Token
#from django.contrib.auth.models import User

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer
    #authentication_classes = (TokenAuthentication,)

    # extra_kwargs = {'password':{
    #     'write_only':True,
    #     'required':True,
    # }}

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     Token.objects.create(user=user)
    #     return user

class TeachersViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeachersSerializer

class AdminsViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminsSerializer

class SubjectsViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectsSerializer