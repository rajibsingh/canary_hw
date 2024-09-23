from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GH_User(models.Model):
    gh_username = models.CharField(max_length=100)
    gh_activerepo = models.CharField(max_length=100)
    gh_sessionkey = models.CharField(max_length=100)

class UserRepository(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='repositories')
    selected_rep = models.JSONField()
    selected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.selected_repo.get('name', 'Unknown Repo')}"


