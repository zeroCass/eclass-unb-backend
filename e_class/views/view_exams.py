from ..models import Exams
from ..serializers.exams_serializer import ExamsSerializer, ExamsSerializerEDIT
from rest_framework import status #type: ignore
from rest_framework.response import Response #type: ignore
from rest_framework.views import APIView #type: ignore
from rest_framework.exceptions import NotFound #type: ignore

class examsList(APIView):
    def get(self, request):
        exams = Exams.objects.all()
        serializer = ExamsSerializer(exams, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExamsSerializerEDIT(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class examsOne(APIView):
    def getObject(self, pk):
        try:
            return Exams.objects.get(pk=pk)
        except Exams.DoesNotExist:
            raise NotFound()
    
    def get(self, request, pk):
        exam = self.getObject(pk)
        serializer = ExamsSerializer(exam)
        return Response(serializer.data)
    
    def put(self, request, pk):
        exam = self.getObject(pk)
        serializer = ExamsSerializerEDIT(exam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        exam = self.getObject(pk)
        serializer = ExamsSerializer(exam)
        exam.delete()
        return Response(serializer.data)
