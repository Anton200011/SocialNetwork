from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields = ('first_name', 'last_name', 'username', 'email', 'telephone_numb',)
        help_texts = {
            'username': 'user',
            'email': None,
        }


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('first_name', 'last_name', 'username', 'email', 'telephone_numb',)
