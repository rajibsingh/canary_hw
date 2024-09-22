
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