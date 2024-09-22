
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
            'origin': request.GET.get('origin', '/')
        }
        return redirect(f"{github_authorize_url}?client_id={params['client_id']}&redirect_uri={params['redirect_uri']}&scope={params['scope']}")

class GitHubCallback(APIView):
    def get(self, request):
        code = request.GET.get('code')
        if not code:
            return Response({'error': 'Authorization code not provided'}, status=status.HTTP_400_BAD_REQUEST)

        # Exchange code for access token
        token_url = "https://github.com/login/oauth/access_token"
        headers = {'Accept': 'application/json'}
        payload = {
            'client_id': settings.GITHUB_CLIENT_ID,
            'client_secret': settings.GITHUB_CLIENT_SECRET,
            'code': code,
            'redirect_uri': 'http://127.0.0.1:8000/gh_connect/callback/',  # Ensure this matches the redirect URI in GitHub settings
        }

        response = requests.post(token_url, headers=headers, data=payload)
        token_data = response.json()

        if 'access_token' not in token_data:
            return Response({'error': 'Failed to retrieve access token'}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch user details with the access token
        access_token = token_data['access_token']
        user_data = requests.get('https://api.github.com/user', headers={
            'Authorization': f'token {access_token}'
        }).json()

        return Response({'message': 'Logged in successfully', 'user': user_data})
