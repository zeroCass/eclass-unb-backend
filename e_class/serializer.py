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
        fields = fieldsUser