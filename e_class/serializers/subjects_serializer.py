from rest_framework import serializers  # type:ignore
from ..models import *
from .teachers_serializer import TeachersSerializer
# from .classes_serializer import ClassesSerializer


class SubjectsSerializer(serializers.ModelSerializer):
    teachers = TeachersSerializer(many=True)
    # classes = ClassesSerializer(many=True)

    class Meta:
        model = Subject
        fields = ["id", "teachers", "name", "description", "classes"]


class SubjectsSerializerEDIT(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            "teachers": {
                "required": False,
            },
            "name": {
                "required": False,
            },
            "description": {
                "required": False,
            },
        }
        model = Subject
        fields = ["id", "teachers", "name", "description"]