from django.shortcuts import redirect, render

from hoods.models import UserProfile
from .forms import ProfileForm,PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login')
def index(request):
  current_user=request.user
  profile=UserProfile.objects.filter(user=current_user).first()
  if request.method=='POST':
    userform=ProfileForm(request.POST)
    if userform.is_valid():
      userprofile=userform.save(commit=False)
      print('Gooo')
      userprofile.user=current_user
      userprofile.save()

    return redirect('home')

  userform=ProfileForm()
  postform=PostForm()
  context={
    'userform':userform,
    'profile':profile,
    'postform':postform
  }
  return render(request,'index.html',context)