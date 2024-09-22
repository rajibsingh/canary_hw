
from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from .models import GH_User
from .serializers import GH_UserSerializer

# Create your views here.
class GH_UserViewSet(viewsets.ModelViewSet):
    queryset = GH_User.objects.all()
    serializer_class = GH_UserSerializer

class LoginEndpoint(APIView):
    def get(self, request):
        # Step 1: Redirect to GitHub's OAuth authorization page
        github_authorize_url = "https://github.com/login/oauth/authorize"
        redirect_uri = request.build_absolute_uri('/gh_connect/callback/')
        params = {
            'client_id': settings.GITHUB_CLIENT_ID,
            'redirect_uri': redirect_uri,
            'scope': 'user',  # Scopes define what access the token will have; adjust as necessary
        }
        return redirect(f"{github_authorize_url}?client_id={params['client_id']}&redirect_uri={params['redirect_uri']}&scope={params['scope']}")

    def post(self, request):
        # Step 1: Redirect to GitHub's OAuth authorization page
        github_authorize_url = "https://github.com/login/oauth/authorize"
        redirect_uri = request.build_absolute_uri('/gh_connect/callback/')
        params = {
            'client_id': settings.GITHUB_CLIENT_ID,
            'redirect_uri': redirect_uri,
            'scope': 'user',  # Scopes define what access the token will have; adjust as necessary
        }
        return redirect(f"{github_authorize_url}?client_id={params['client_id']}&redirect_uri={params['redirect_uri']}&scope={params['scope']}")

        # return Response({'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        # data = {"message": "This is the POST login"}
        # email = request.data.get('email')
        # password = request.data.get('password')
        #
        # if email == "testuser@gmail.com" and password == "password":
        #     data["message"] = "Login successful"
        #     return Response(data, status=status.HTTP_200_OK)
        # else:
        #     data["message"] = "Login failed"
        #     return Response(data, status=status.HTTP_403_FORBIDDEN)