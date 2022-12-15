from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'user_name',
            'user_city'

        )
        widgets = {
            'user_name': forms.TextInput,
            'User_city': forms.TextInput
        }
