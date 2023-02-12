from ..models import Subject
from ..serializer import SubjectsSerializer, SubjectsSerializerEDIT
from rest_framework import status #type: ignore
from rest_framework.response import Response #type: ignore
from rest_framework.views import APIView #type: ignore
from rest_framework.exceptions import NotFound #type: ignore

class subjectsList(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectsSerializer(subjects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubjectsSerializerEDIT(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class subjectsOne(APIView):
    def getObject(self, pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            raise NotFound()
    
    def get(self, pk):
        subject = self.getObject(pk)
        serializer = SubjectsSerializer(subject)
        return Response(serializer.data)
    
    def put(self, request, pk):
        subject = self.getObject(pk)
        serializer = SubjectsSerializerEDIT(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, pk):
        subject = self.getObject(pk)
        serializer = SubjectsSerializer(subject)
        subject.delete()
        return Response(serializer.data)
