from django.contrib import admin
from .models import Post, UserProfile,Business,NeighbourHood,Contact
# Register your models here.

class BusinessAdmin(admin.ModelAdmin):
  list_display=['name','profile','neighbourhood','email','created_at']

class NeighbourhoodAdmin(admin.ModelAdmin):
  list_display=['name','location','occupants_count','admin','image','created_at']

class ContactAdmin(admin.ModelAdmin):
  list_display=['title','phone','email','neighbourhood']

class PostAdmin(admin.ModelAdmin):
  list_display=['title','profile','neighbourhood','image','content','created_at']

class UserProfileAdmin(admin.ModelAdmin):
  list_display=['name','national_id','user','neighbourhood','email','created_at']

admin.site.register(UserProfile,)
admin.site.register(Business,BusinessAdmin)
admin.site.register(NeighbourHood,NeighbourhoodAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Contact,ContactAdmin)