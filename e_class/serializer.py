from rest_framework import serializers #type:ignore
from .models import Users
from random import randint

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','name','email','password','cpf','userType']