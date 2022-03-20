from django.shortcuts import render
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login')
def index(request):
  form=ProfileForm()
  context={
    'form':form,
  }
  return render(request,'index.html',context)