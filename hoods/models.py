from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class NeighbourHood(models.Model):
  name=models.CharField(max_length=500)
  location=models.CharField(max_length=500)
  occupants_count=models.IntegerField()
  admin=models.ForeignKey(User,related_name='neighbourhood',on_delete=models.CASCADE)


class UserProfile(models.Model):
  name=models.CharField(max_length=100)
  national_id=models.IntegerField()
  neighbourhood=models.OneToOneField(NeighbourHood,related_name='profile',on_delete=models.CASCADE)
  email=models.EmailField()

class Business(models.Model):
  name=models.CharField(max_length=200)
  profile=models.ForeignKey(UserProfile,related_name='business',on_delete=models.CASCADE)
  neighbourhood=models.ForeignKey(NeighbourHood,related_name='business',on_delete=models.CASCADE)
  email=models.EmailField()

