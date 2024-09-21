from rest_framework import serializers
from .models import GH_User

class GH_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GH_User
        fields = ['gh_username', 'gh_activerepo', 'gh_sessionkey']
