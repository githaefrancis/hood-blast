from django.shortcuts import render
from .forms import ProfileForm
# Create your views here.

def index(request):
  form=ProfileForm()
  context={
    'form':form,
  }
  return render(request,'index.html',context)