from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import datetime

# Create your models here.

class NeighbourHood(models.Model):
  name=models.CharField(max_length=500)
  location=models.CharField(max_length=500)
  occupants_count=models.IntegerField()
  admin=models.ForeignKey(User,related_name='neighbourhood',on_delete=models.CASCADE)
  created_at=models.DateTimeField(auto_now_add=True)



class UserProfile(models.Model):
  name=models.CharField(max_length=100)
  national_id=models.IntegerField()
  user=models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
  neighbourhood=models.ForeignKey(NeighbourHood,related_name='occupant',on_delete=models.CASCADE)
  email=models.EmailField()
  created_at=models.DateTimeField(auto_now_add=True)


class Business(models.Model):
  name=models.CharField(max_length=200)
  profile=models.ForeignKey(UserProfile,related_name='business',on_delete=models.CASCADE)
  neighbourhood=models.ForeignKey(NeighbourHood,related_name='business',on_delete=models.CASCADE)
  email=models.EmailField()
  created_at=models.DateTimeField(auto_now_add=True)


class Post(models.Model):
  title=models.CharField(max_length=200)
  image=CloudinaryField('image')
  content=models.TextField()
  created_at=models.DateTimeField(auto_now_add=True)
