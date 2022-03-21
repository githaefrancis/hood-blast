
from django.http import Http404
from django.shortcuts import redirect, render

from hoods.models import Business, Contact, NeighbourHood, UserProfile,Post
from .forms import BusinessForm, ProfileForm,PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login')
def index(request):
  current_user=request.user
  profile=UserProfile.objects.filter(user=current_user).first()
  
  if request.method=='POST':
    userform=ProfileForm(request.POST)
    postform=PostForm(request.POST,request.FILES)
    businessform=BusinessForm(request.POST)

    if userform.is_valid():
      userprofile=userform.save(commit=False)
      userprofile.user=current_user
      userprofile.save()
    

    if postform.is_valid():
      new_post=postform.save(commit=False)
      new_post.profile=profile
      new_post.neighbourhood=profile.neighbourhood
      new_post.save()
      
    if businessform.is_valid():
      new_business=businessform.save(commit=False)
      new_business.profile=profile
      new_business.save()
    

    return redirect('home')
  try:
    posts=Post.objects.filter(neighbourhood=profile.neighbourhood)
    businesses=Business.objects.filter(neighbourhood=profile.neighbourhood)
  except:
    posts=[]
    businesses=[]
  userform=ProfileForm()
  postform=PostForm()
  businessform=BusinessForm()
  context={
    'userform':userform,
    'profile':profile,
    'postform':postform,
    'businessform':businessform,
    'posts':posts,
    'businesses':businesses
  }
  return render(request,'index.html',context)


@login_required(login_url='/accounts/login')
def search(request):
  if 'search' in request.GET and request.GET['search']:
    try:
      search_word=request.GET.get('search')
      post_results=Post.search_posts(search_word,request.user.profile.neighbourhood)

      context={
      'posts':post_results
      }

      return render(request,'search.html',context)
    except ValueError:
      return Http404


@login_required(login_url='accounts/login')
def contact(request):
  current_user=request.user
  try:
    profile=UserProfile.objects.filter(user=current_user).first()
    contacts=Contact.objects.filter(neighbourhood=profile.neighbourhood).all()
  except:
    contacts=[]
  print(profile)
  context={
    'contacts':contacts
  }
  return render(request,'contact.html',context)