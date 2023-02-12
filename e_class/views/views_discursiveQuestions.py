from ..models import DiscursiveQuestion
from ..serializers.questions_serializer import DiscursiveQuestionSerializer, DiscursiveQuestionSerializerEDIT
from rest_framework import status #type: ignore
from rest_framework.response import Response #type: ignore
from rest_framework.views import APIView #type: ignore
from rest_framework.exceptions import NotFound #type: ignore

class discursiveQuestionsList(APIView):
    def get(self, request):
        discursiveQuestions = DiscursiveQuestion.objects.all()
        serializer = DiscursiveQuestionSerializer(discursiveQuestions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DiscursiveQuestionSerializerEDIT(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class discursiveQuestionsOne(APIView):
    def getObject(self, pk):
        try:
            return DiscursiveQuestion.objects.get(pk=pk)
        except DiscursiveQuestion.DoesNotExist:
            raise NotFound()
    
    def get(self, request, pk):
        discursiveQuestion = self.getObject(pk)
        serializer = DiscursiveQuestionSerializer(discursiveQuestion)
        return Response(serializer.data)
    
    def put(self, request, pk):
        discursiveQuestion = self.getObject(pk)
        serializer = DiscursiveQuestionSerializerEDIT(discursiveQuestion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        discursiveQuestion = self.getObject(pk)
        serializer = DiscursiveQuestionSerializer(discursiveQuestion)
        discursiveQuestion.delete()
        return Response(serializer.data)
