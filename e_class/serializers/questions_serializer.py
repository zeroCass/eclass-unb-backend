from rest_framework import serializers  # type:ignore
from ..models import *
# from .students_serializer import StudentsSerializer
# from .teachers_serializer import TeachersSerializer


class MultipleQuestionSerializer(serializers.ModelSerializer):
    # students = StudentsSerializer(many=True)
    # teacher = TeachersSerializer()

    class Meta:
        model = MultipleQuestion
        fields = [
            "id",
            "name",
            "is_visibility",
            "statement",
            "students",
            "teacher",
            "option1",
            "option2",
            "option3",
            "option4",
            "answer",
        ]


class MultipleQuestionSerializerEDIT(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            "name": {
                "required": False,
            },
            "is_visibility": {
                "required": False,
            },
            "statement": {
                "required": False,
            },
            "students": {
                "required": False,
            },
            "teacher": {
                "required": False,
            },
            "option1": {
                "required": False,
            },
            "option2": {
                "required": False,
            },
            "option3": {
                "required": False,
            },
            "option4": {
                "required": False,
            },
            "answer": {
                "required": False,
            },
        }
        model = MultipleQuestion
        fields = [
            "id",
            "name",
            "is_visibility",
            "statement",
            "students",
            "teacher",
            "option1",
            "option2",
            "option3",
            "option4",
            "answer",
        ]


class DiscursiveQuestionSerializer(serializers.ModelSerializer):
    # students = StudentsSerializer(many=True)
    # teacher = TeachersSerializer()

    class Meta:
        model = DiscursiveQuestion
        fields = [
            "id",
            "name",
            "is_visibility",
            "statement",
            "students",
            "teacher",
            "answer",
        ]


class DiscursiveQuestionSerializerEDIT(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            "name": {
                "required": False,
            },
            "is_visibility": {
                "required": False,
            },
            "statement": {
                "required": False,
            },
            "students": {
                "required": False,
            },
            "teacher": {
                "required": False,
            },
            "answer": {
                "required": False,
            },
        }
        model = DiscursiveQuestion
        fields = [
            "id",
            "name",
            "is_visibility",
            "statement",
            "students",
            "teacher",
            "answer",
        ]