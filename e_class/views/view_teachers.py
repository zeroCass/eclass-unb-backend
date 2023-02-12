from ..models import Teacher
from ..serializers.teachers_serializer import TeachersSerializer, TeachersSerializerEDIT
from rest_framework import status #type: ignore
from rest_framework.response import Response #type: ignore
from rest_framework.views import APIView #type: ignore
from rest_framework.exceptions import NotFound #type: ignore
from django.contrib.auth.models import User  # type: ignore


class teachersList(APIView):
    def get(self, request):
        students = Teacher.objects.all()
        serializer = TeachersSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data["userType"] = 2
        serializer = TeachersSerializerEDIT(data=request.data)
        if serializer.is_valid():
            User.objects.create(
                username=request.data["name"],
                email=request.data["email"],
                password=request.data["password"],
            )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class teacherOne(APIView):
    def getObject(self, pk):
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            raise NotFound()
    
    def get(self, request, pk):
        student = self.getObject(pk)
        serializer = TeachersSerializer(student)
        return Response(serializer.data)
    
    def put(self, request, pk):
        request.data["userType"] = 2
        student = self.getObject(pk)
        serializer = TeachersSerializerEDIT(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        student = self.getObject(pk)
        serializer = TeachersSerializer(student)
        student.delete()
        return Response(serializer.data)
