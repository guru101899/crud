from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100,unique=True)
    password=models.CharField(max_length=128)

# just adding a comment to see the pull request