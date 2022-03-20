from django.contrib import admin
from .models import Post, UserProfile,Business,NeighbourHood
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Business)
admin.site.register(NeighbourHood)
admin.site.register(Post)