from django.urls import path,re_path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    re_path('^search/',views.search,name='search'),
    re_path('^contacts/',views.contact,name='contact'),
    re_path('^profile/',views.profile,name='profile')
]

