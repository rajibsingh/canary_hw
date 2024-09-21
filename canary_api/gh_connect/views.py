
from pprint import pprint
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import GH_User
from .serializers import GH_UserSerializer

# Create your views here.
class GH_UserViewSet(viewsets.ModelViewSet):
    queryset = GH_User.objects.all()
    serializer_class = GH_UserSerializer

class LoginEndpoint(APIView):
    def get(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        data = {"message": "This is the POST login"}
        email = request.data.get('email')
        password = request.data.get('password')

        if email == "testuser@gmail.com" and password == "password":
            data["message"] = "Login successful"
            return Response(data, status=status.HTTP_200_OK)
        else:
            data["message"] = "Login failed"
            return Response(data, status=status.HTTP_403_FORBIDDEN)