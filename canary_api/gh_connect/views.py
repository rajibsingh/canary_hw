
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
        data = {"message": "This is the GET login"}
        pprint(request)
        return Response(data, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        data = {"message": "This is the POST login"}
        pprint(request)
        return Response(data, status=status.HTTP_200_OK)

