from .models import UserProfile,Post
from django.forms import ModelForm

class ProfileForm(ModelForm):
  class Meta:
    model=UserProfile
    exclude=['user','created_at',]


class PostForm(ModelForm):
  class Meta:
    model=Post
    exclude=['created_at','profile']