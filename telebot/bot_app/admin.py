from django.contrib import admin
# from .forms import UserProfileForm
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id','first_name','last_name','user_city')

