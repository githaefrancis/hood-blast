from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import datetime

# Create your models here.

class NeighbourHood(models.Model):
  name=models.CharField(max_length=500)
  location=models.CharField(max_length=500)
  occupants_count=models.IntegerField(default=0)
  admin=models.ForeignKey(User,related_name='neighbourhood',on_delete=models.CASCADE)
  image=CloudinaryField('image',blank=True,null=True)
  created_at=models.DateTimeField(auto_now_add=True)

  def create_neighbourhood(self):
    '''
    Method to create a new neighbourhood
    '''
    self.save()
  @classmethod
  def find_neighbourhood(cls,id):
    '''
    Method to retrieve a neighbourhood by id
    '''
    return cls.objects.filter(id=id).first()

  def update_neighbourhood(self,**kwargs):
    '''
    Method to update neighbourhood details
    '''
    for key,value in kwargs.items():
      setattr(self,key,value)
    self.save()
    return 
  def delete_neighbourhood(self):
    self.delete()


  def update_occupants(self):
    occupants=len(UserProfile.objects.filter(neighbourhood=self).all())
    self.occupants_count=occupants
    return occupants

  def __str__(self):
    return self.name

class UserProfile(models.Model):
  name=models.CharField(max_length=100)
  national_id=models.IntegerField()
  user=models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
  neighbourhood=models.ForeignKey(NeighbourHood,related_name='occupant',on_delete=models.CASCADE)
  email=models.EmailField()
  created_at=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name


class Business(models.Model):
  name=models.CharField(max_length=200)
  profile=models.ForeignKey(UserProfile,related_name='business',on_delete=models.CASCADE)
  neighbourhood=models.ForeignKey(NeighbourHood,related_name='business',on_delete=models.CASCADE)
  email=models.EmailField()
  created_at=models.DateTimeField(auto_now_add=True)

  def create_business(self):
    self.save()

  @classmethod
  def find_business(cls,id):
    return cls.objects.filter(id=id).first()

  def update_business(self,**kwargs):
    for key,value in kwargs.items():
      setattr(self,key,value)
    self.save()
    return self
    
  def __str__(self):
    return self.name
  

class Post(models.Model):
  title=models.CharField(max_length=200)
  profile=models.ForeignKey(UserProfile,related_name='post',on_delete=models.CASCADE,default=None)
  neighbourhood=models.ForeignKey(NeighbourHood,related_name='post',on_delete=models.CASCADE,default=None)
  image=CloudinaryField('image',default=None)
  content=models.TextField()
  created_at=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

  @classmethod
  def search_posts(cls,search_word,neighbourhood):
    return cls.objects.filter(title__icontains=search_word,neighbourhood=neighbourhood)


class Contact(models.Model):
  title=models.CharField(max_length=100)
  phone=models.CharField(max_length=20)
  email=models.EmailField()
  neighbourhood=models.ForeignKey(NeighbourHood,related_name='contact',on_delete=models.CASCADE,default=None)
  

  def __str__(self):
    return self.title