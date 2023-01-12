from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    firstName = forms.CharField(label="First Name", max_length=50)
    lastName = forms.CharField(label="Last Name", max_length=50)
    email = forms.EmailField(max_length=200)
    avatar = forms.CharField(max_length=500, required=False)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "firstName",
            "lastName",
            "username",
            "email",
            "avatar",
            "password1",
            "password2",
        )  # type: ignore


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
