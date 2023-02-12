from rest_framework import status, authentication, permissions  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework.views import APIView  # type: ignore
from rest_framework.authtoken.models import Token  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from ..models import Student, Teacher, Admin
from ..serializers.students_serializer import StudentsSerializer
from ..serializers.teachers_serializer import TeachersSerializer
from ..serializers.admins_serializer import AdminsSerializer


class login(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({"message": "método errado"})

    def post(self, request):
        try:
            email = request.data["email"]
            password = request.data["password"]
            user = User.objects.get(email=email)
            if password == user.password:
                try:
                    student = Student.objects.get(email=email)
                    serializer = StudentsSerializer(student)
                except:
                    pass
                try:
                    teacher = Teacher.objects.get(email=email)
                    serializer = TeachersSerializer(teacher)
                except:
                    pass
                try:
                    admin = Admin.objects.get(email=email)
                    serializer = AdminsSerializer(admin)
                except:
                    pass
                try:
                    token = Token.objects.get(user=user)
                except:
                    token = Token.objects.create(user=user)
                return Response({"token": token.key, "user": serializer.data})
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class logout(APIView):
    def get(self, request):
        return Response({"message": "método errado"})
    
    def post(self, request):
        try:
            email = request.data["email"]
            user = User.objects.get(email=email)
            token = Token.objects.get(user=user)
            token.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)