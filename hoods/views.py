
from django.shortcuts import redirect, render

from hoods.models import UserProfile
from .forms import BusinessForm, ProfileForm,PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login')
def index(request):
  current_user=request.user
  profile=UserProfile.objects.filter(user=current_user).first()
  if request.method=='POST':
    userform=ProfileForm(request.POST)
    postform=PostForm(request.POST)
    businessform=BusinessForm(request.POST)
    if userform.is_valid():
      userprofile=userform.save(commit=False)
      userprofile.user=current_user
      userprofile.save()

    if postform.is_valid():
      new_post=postform.save(commit=False)
      new_post.profile=profile
      new_post.save()
      
    if businessform.is_valid():
      new_business=businessform.save(commit=False)
      new_business.profile=profile
      new_business.save()

    return redirect('home')

  userform=ProfileForm()
  postform=PostForm()
  businessform=BusinessForm()
  context={
    'userform':userform,
    'profile':profile,
    'postform':postform,
    'businessform':businessform
  }
  return render(request,'index.html',context)