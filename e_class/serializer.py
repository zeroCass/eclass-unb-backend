from rest_framework import serializers #type:ignore
from .models import Student
from random import randint

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','email','password','cpf','userType']