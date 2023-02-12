from ..models import Student
from ..serializer import StudentsSerializer, StudentsSerializerEDIT
from rest_framework import status #type: ignore
from rest_framework.response import Response #type: ignore
from rest_framework.views import APIView #type: ignore
from rest_framework.exceptions import NotFound #type: ignore
from django.contrib.auth.models import User  # type: ignore

class studentsList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentsSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentsSerializerEDIT(data=request.data)
        if serializer.is_valid():
            User.objects.create(
                username=request.data["name"],
                email=request.data["email"],
                password=request.data["password"],
            )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class studentOne(APIView):
    def getObject(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise NotFound()
    
    def get(self, pk):
        student = self.getObject(pk)
        serializer = StudentsSerializer(student)
        return Response(serializer.data)
    
    def put(self, request, pk):
        student = self.getObject(pk)
        serializer = StudentsSerializerEDIT(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, pk):
        student = self.getObject(pk)
        serializer = StudentsSerializer(student)
        student.delete()
        return Response(serializer.data)
