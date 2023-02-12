from rest_framework import serializers  # type:ignore
from ..models import *
from .subjects_serializer import SubjectsSerializer
# from .students_serializer import StudentsSerializer
from .teachers_serializer import TeachersSerializerByClass
from .exams_serializer import ExamsSerializer


class ClassesSerializer(serializers.ModelSerializer):
    subject = SubjectsSerializer()
    # students = StudentsSerializer(many=True)
    teachers = TeachersSerializerByClass(many=True)
    exams = ExamsSerializer(many=True)

    class Meta:
        model = Classes
        fields = [
            "id",
            "subject",
            "students",
            "teachers",
            "name",
            "size",
            "startTime",
            "endTime",
            "period",
            "password",
            "createdAt",
            "exams",
        ]


class ClassesSerializerEDIT(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            "subject": {
                "required": False,
            },
            "students": {
                "required": False,
            },
            "teachers": {
                "required": False,
            },
            "name": {
                "required": False,
            },
            "size": {
                "required": False,
            },
            "startTime": {
                "required": False,
            },
            "endTime": {
                "required": False,
            },
            "period": {
                "required": False,
            },
            "password": {
                "required": False,
            },
            "createdAt": {
                "required": False,
            },
            "exams": {
                "required": False,
            },
        }
        model = Classes
        fields = [
            "id",
            "subject",
            "students",
            "teachers",
            "name",
            "size",
            "startTime",
            "endTime",
            "period",
            "password",
            "createdAt",
            "exams",
        ]