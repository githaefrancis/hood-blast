from .models import UserProfile
from django.forms import ModelForm

class ProfileForm(ModelForm):
  class Meta:
    model=UserProfile
    exclude=['user','created_at',]