from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
"""!@ Creates Custom User Creation Form.
"""

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(forms.ModelForm):
"""!@ Creates Custom User Change Form.
"""

    class Meta:
        model = CustomUser
        fields = ('password',)
        exclude = ("username", "email",)

    # def clean_username(self):
    #     return self.username
    #
    # def clean_email(self):
    #     return self.email





