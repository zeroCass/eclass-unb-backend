from rest_framework import serializers  # type:ignore
from ..models import *
# from .subjects_serializer import SubjectsSerializer


class AdminsSerializer(serializers.ModelSerializer):
    # subjects = SubjectsSerializer(many=True)

    class Meta:
        model = Admin
        fields = ["id", "name", "email", "cpf", "userType", "subjects"]


class AdminsSerializerEDIT(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            "name": {
                "required": False,
            },
            "email": {
                "required": False,
            },
            "password": {
                "required": False,
            },
            "cpf": {
                "required": False,
            },
            "userType": {
                "required": False,
            },
        }
        model = Admin
        fields = ["id", "name", "email", "password", "cpf", "userType"]