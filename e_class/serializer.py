from rest_framework import serializers #type:ignore
from .models import *

fieldsUser = ['id','name','email','password','cpf','userType']

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = fieldsUser

class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = fieldsUser + ['specialization']

class AdminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = fieldsUser

class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'teachers', 'course', 'description']