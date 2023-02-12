from rest_framework import serializers  # type:ignore
from ..models import *
from .questions_serializer import (
    MultipleQuestionSerializer,
    DiscursiveQuestionSerializer,
)
from .exams_serializer import ExamsSerializer


class TeachersSerializerByClass(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            "id",
            "name",
            "email",
            "cpf",
            "password",
            "userType",
            "specialization",
            "subjects",
            "classes",
        ]


class TeachersSerializer(serializers.ModelSerializer):
    multipleQuestions = MultipleQuestionSerializer(many=True)
    discursiveQuestions = DiscursiveQuestionSerializer(many=True)
    exams = ExamsSerializer(many=True)

    class Meta:
        model = Teacher
        fields = [
            "id",
            "name",
            "email",
            "cpf",
            "password",
            "userType",
            "specialization",
            "subjects",
            "classes",
            "multipleQuestions",
            "discursiveQuestions",
            "exams",
        ]


class TeachersSerializerEDIT(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            "name": {
                "required": False,
            },
            "email": {
                "required": False,
            },
            "cpf": {
                "required": False,
            },
            "password": {
                "required": False,
            },
            "userType": {
                "required": False,
            },
            "specialization": {
                "required": False,
            },
            "subjects": {
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
            "exams": {
                "required": False,
            },
        }
        model = Teacher
        fields = [
            "id",
            "name",
            "email",
            "cpf",
            "password",
            "userType",
            "specialization",
            "subjects",
            "classes",
            "multipleQuestions",
            "discursiveQuestions",
            "exams",
        ]
