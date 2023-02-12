from rest_framework import serializers  # type:ignore
from ..models import *
from .classes_serializer import ClassesSerializer
from .questions_serializer import (
    MultipleQuestionSerializer,
    DiscursiveQuestionSerializer,
)


class StudentsSerializer(serializers.ModelSerializer):
    classes = ClassesSerializer(many=True)
    multipleQuestions = MultipleQuestionSerializer(many=True)
    discursiveQuestions = DiscursiveQuestionSerializer(many=True)

    class Meta:
        model = Student
        fields = [
            "id",
            "name",
            "email",
            "password",
            "cpf",
            "userType",
            "classes",
            "multipleQuestions",
            "discursiveQuestions",
        ]


class StudentsSerializerEDIT(serializers.ModelSerializer):
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
            "classes": {
                "required": False,
            },
            "multipleQuestions": {
                "required": False,
            },
            "discursiveQuestions": {
                "required": False,
            },
        }
        model = Student
        fields = [
            "id",
            "name",
            "email",
            "password",
            "cpf",
            "userType",
            "classes",
            "multipleQuestions",
            "discursiveQuestions",
        ]
