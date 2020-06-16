from django.db import models
from django.contrib.auth.models import User
class Result(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    result = models.IntegerField()
  