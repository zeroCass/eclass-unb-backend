from rest_framework import serializers  # type:ignore
from .models import *

fieldsUserEDIT = ["id", "name", "email", "password", "cpf", "userType"]
fieldsUserGET = ["id", "name", "email", "cpf", "userType"]


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = fieldsUserGET


class StudentsSerializerEDIT(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            "name": {"required": False,},
            "email": {"required": False,},
            "password": {"required": False,},
            "cpf": {"required": False,},
            "userType": {"required": False,},
        }
        model = Student
        fields = fieldsUserEDIT


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = fieldsUserGET + ["specialization"]


class TeachersSerializerEDIT(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = fieldsUserEDIT + ["specialization"]


class AdminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = fieldsUserGET


class AdminsSerializerEDIT(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = fieldsUserEDIT


class SubjectsSerializer(serializers.ModelSerializer):
    teachers = TeachersSerializer(many=True)

    class Meta:
        model = Subject
        fields = ["id", "teachers", "name", "description"]


class SubjectsSerializerEDIT(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id", "teachers", "course", "description"]


class ClassesSerializer(serializers.ModelSerializer):
    subject = SubjectsSerializer()
    students = StudentsSerializer(many=True)
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


class MultipleQuestionSerializer(serializers.ModelSerializer):
    students = StudentsSerializer(many=True)
    teacher = TeachersSerializer()

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
    students = StudentsSerializer(many=True)
    teacher = TeachersSerializer()

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


class ExamsSerializer(serializers.ModelSerializer):
    multipleQuestions = MultipleQuestionSerializer(many=True)
    discursiveQuestions = DiscursiveQuestionSerializer(many=True)
    students = StudentsSerializer(many=True)
    teacher = TeachersSerializer()

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
        ]


class ExamsSerializerEDIT(serializers.ModelSerializer):
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
        ]