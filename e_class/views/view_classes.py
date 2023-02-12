from ..models import Classes
from ..serializer import ClassesSerializer, ClassesSerializerEDIT
from rest_framework import status #type: ignore
from rest_framework.response import Response #type: ignore
from rest_framework.views import APIView #type: ignore
from rest_framework.exceptions import NotFound #type: ignore

class classesList(APIView):
    def get(self, request):
        classes = Classes.objects.all()
        serializer = ClassesSerializer(classes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassesSerializerEDIT(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class classesOne(APIView):
    def getObject(self, pk):
        try:
            return Classes.objects.get(pk=pk)
        except Classes.DoesNotExist:
            raise NotFound()
    
    def get(self, pk):
        classe = self.getObject(pk)
        serializer = ClassesSerializer(classe)
        return Response(serializer.data)
    
    def put(self, request, pk):
        classe = self.getObject(pk)
        serializer = ClassesSerializerEDIT(classe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, pk):
        classe = self.getObject(pk)
        serializer = ClassesSerializer(classe)
        classe.delete()
        return Response(serializer.data)
