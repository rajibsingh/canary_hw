from django.db import models

# Create your models here.
class GH_User(models.Model):
    gh_username = models.CharField(max_length=100)
    gh_activerepo = models.CharField(max_length=100)
    gh_sessionkey = models.CharField(max_length=100)