from rest_framework import serializers  # type:ignore
from ..models import *
from .questions_serializer import MultipleQuestionSerializer, DiscursiveQuestionSerializer
# from .students_serializer import StudentsSerializer
# from .teachers_serializer import TeachersSerializer


class ExamsSerializer(serializers.ModelSerializer):
    multipleQuestions = MultipleQuestionSerializer(many=True)
    discursiveQuestions = DiscursiveQuestionSerializer(many=True)
    # students = StudentsSerializer(many=True)
    # teacher = TeachersSerializer()

    class Meta:
        model = Exams
        fields = [
            "id",
            "name",
            "startAt",
            "endedAt",
            "isVisible",
            "score",
            "multipleQuestions",
            "discursiveQuestions",
            "students",
            "teacher",
            "classe",
        ]


class ExamsSerializerEDIT(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            "name": {
                "required": False,
            },
            "startAt": {
                "required": False,
            },
            "endedAt": {
                "required": False,
            },
            "isVisible": {
                "required": False,
            },
            "score": {
                "required": False,
            },
            "multipleQuestions": {
                "required": False,
            },
            "discursiveQuestions": {
                "required": False,
            },
            "students": {
                "required": False,
            },
            "teacher": {
                "required": False,
            },
        }
        model = Exams
        fields = [
            "id",
            "name",
            "startAt",
            "endedAt",
            "isVisible",
            "score",
            "multipleQuestions",
            "discursiveQuestions",
            "students",
            "teacher",
        ]