from rest_framework import serializers #type:ignore
from .models import *

fieldsUser = ['id','name','email','password','cpf','userType']

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = fieldsUser

class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = fieldsUser + ['specialization']

class AdminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = fieldsUser

class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'teachers', 'course', 'description']

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ['id', 'subject', 'students', 'teachers', 'name', 'size', 'startTime', 'endTime', 'period', 'password', 'createdAt']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['is_visibility', 'statement', 'students', 'teacher']

class MultipleQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleQuestion
        fields = ['id', 'option1', 'option2', 'option3', 'option4', 'answer', 'is_visibility', 'statement', 'students', 'teacher']

class DiscursiveQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscursiveQuestion
        fields = ['id', 'answer', 'is_visibility', 'statement', 'students', 'teacher']

class ExamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exams
        fields = ['id', 'startAt', 'endedAt', 'isVisible', 'score', 'multipleQuestions', 'discursiveQuestions', 'students', 'teacher']
