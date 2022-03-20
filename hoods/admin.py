from django.contrib import admin
from .models import Post, UserProfile,Business,NeighbourHood
# Register your models here.

class BusinessAdmin(admin.ModelAdmin):
  list_display=['name','profile','neighbourhood','email','created_at']

admin.site.register(UserProfile)
admin.site.register(Business,BusinessAdmin)
admin.site.register(NeighbourHood)
admin.site.register(Post)