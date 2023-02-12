from ..models import Admin
from ..serializer import AdminsSerializer, AdminsSerializerEDIT
from rest_framework import status #type: ignore
from rest_framework.response import Response #type: ignore
from rest_framework.views import APIView #type: ignore
from rest_framework.exceptions import NotFound #type: ignore
from django.contrib.auth.models import User  # type: ignore


class adminsList(APIView):
    def get(self, request):
        students = Admin.objects.all()
        serializer = AdminsSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdminsSerializerEDIT(data=request.data)
        if serializer.is_valid():
            User.objects.create(
                username=request.data["name"],
                email=request.data["email"],
                password=request.data["password"],
            )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class adminOne(APIView):
    def getObject(self, pk):
        try:
            return Admin.objects.get(pk=pk)
        except Admin.DoesNotExist:
            raise NotFound()
    
    def get(self, request, pk):
        student = self.getObject(pk)
        serializer = AdminsSerializer(student)
        return Response(serializer.data)
    
    def put(self, request, pk):
        student = self.getObject(pk)
        serializer = AdminsSerializerEDIT(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        student = self.getObject(pk)
        serializer = AdminsSerializer(student)
        student.delete()
        return Response(serializer.data)
