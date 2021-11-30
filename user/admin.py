from django.contrib import admin
from django.contrib.auth.models import User
from .models import Post,UserProfile

@admin.register(Post)
class UserAdmin(admin.ModelAdmin):
     list_display = ('id','postusername' , 'postname', 'description')

@admin.register(UserProfile)
class UserAdmin1(admin.ModelAdmin):
     list_display = ('id','username' , 'email', 'birthdate','mobileno','gender', 'city', 'pincode','profile','document')
