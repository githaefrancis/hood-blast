from .models import UserProfile,Post,Business
from django.forms import ModelForm

class ProfileForm(ModelForm):
  class Meta:
    model=UserProfile
    exclude=['user','created_at',]


class PostForm(ModelForm):
  class Meta:
    model=Post
    exclude=['created_at','profile','neighbourhood']

class BusinessForm(ModelForm):
  class Meta:
    model=Business
    exclude=['profile','created_at']