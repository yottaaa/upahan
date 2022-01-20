from django.contrib import admin

from account.models import Profile, UserLogin
# Register your models here.

admin.site.register(Profile)
admin.site.register(UserLogin)