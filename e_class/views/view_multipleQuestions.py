from ..models import MultipleQuestion
from ..serializers.questions_serializer import MultipleQuestionSerializer, MultipleQuestionSerializerEDIT
from rest_framework import status #type: ignore
from rest_framework.response import Response #type: ignore
from rest_framework.views import APIView #type: ignore
from rest_framework.exceptions import NotFound #type: ignore

class multipleQuestionsList(APIView):
    def get(self, request):
        multipleQuestions = MultipleQuestion.objects.all()
        serializer = MultipleQuestionSerializer(multipleQuestions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MultipleQuestionSerializerEDIT(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class multipleQuestionsOne(APIView):
    def getObject(self, pk):
        try:
            return MultipleQuestion.objects.get(pk=pk)
        except MultipleQuestion.DoesNotExist:
            raise NotFound()
    
    def get(self, request, pk):
        multipleQuestion = self.getObject(pk)
        serializer = MultipleQuestionSerializer(multipleQuestion)
        return Response(serializer.data)
    
    def put(self, request, pk):
        multipleQuestion = self.getObject(pk)
        serializer = MultipleQuestionSerializerEDIT(multipleQuestion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        multipleQuestion = self.getObject(pk)
        serializer = MultipleQuestionSerializer(multipleQuestion)
        multipleQuestion.delete()
        return Response(serializer.data)
