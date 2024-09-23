
from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User  # Import Django's User model
from django.contrib.auth import login  # Import login function to log in the user
from django.conf import settings
from .models import UserRepository
import requests

import pprint

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
            'redirect_uri': 'http://localhost:8000/gh_connect/callback/'
        }

        response = requests.post(token_url, headers=headers, data=payload)
        token_data = response.json()

        if 'access_token' not in token_data:
            return Response({'error': 'Failed to retrieve access token'}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch user details with the access token
        access_token = token_data['access_token']

        # Handle creation of Django User and GH_User
        # Fetch the user's GitHub profile using the access token
        user_data = requests.get('https://api.github.com/user', headers={
            'Authorization': f'token {access_token}'
        }).json()

        # Extract relevant information from the GitHub user data
        github_username = user_data.get('login')  # GitHub username
        github_email = user_data.get('email')  # GitHub email (maybe None)

        # Create a unique username for Django based on GitHub username
        username = github_username if github_username else f"github_{user_data['id']}"

        print("**** username: ", username)

        # Check if the user already exists in Django based on the username or email
        user, created = User.objects.get_or_create(
            username=username,
            defaults={'email': github_email if github_email else f"{username}@example.com"}
        )

        if created:
            # If the user was created, you can set additional fields or save the user
            user.set_unusable_password()  # Optional: Set an unusable password since OAuth is used
            user.save()

        # Log the user in (if applicable)
        login(request, user)

        # Redirect to the frontend Home page with the access token
        frontend_redirect_url = f"http://localhost:5173/home?token={access_token}"  # Adjust URL as needed
        return redirect(frontend_redirect_url)

class SaveRepository(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated before saving

    def post(self, request):
        user = request.user  # Get the currently logged-in user
        selected_repo = request.data.get('selected_repo')  # Expecting the repository data as JSON

        # Validate the input
        if not selected_repo:
            return Response({'error': 'Repository data is missing'}, status=status.HTTP_400_BAD_REQUEST)

        # Create or update the UserRepository object linked to the current user
        UserRepository.objects.create(
            user=user,
            selected_repo=selected_repo
        )

        return Response({'message': 'Repository saved successfully!'}, status=status.HTTP_201_CREATED)


