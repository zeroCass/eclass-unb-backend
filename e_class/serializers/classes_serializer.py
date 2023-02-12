from rest_framework import serializers  # type:ignore
from ..models import *
from .subjects_serializer import SubjectsSerializer
# from .students_serializer import StudentsSerializer
from .teachers_serializer import TeachersSerializer


class ClassesSerializer(serializers.ModelSerializer):
    subject = SubjectsSerializer()
    # students = StudentsSerializer(many=True)
    teachers = TeachersSerializer(many=True)

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
        ]