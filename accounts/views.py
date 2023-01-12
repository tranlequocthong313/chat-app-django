from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver


# @receiver(user_logged_in)
# def got_online(sender, user, request, **kwargs):
#     user.profile.is_online = True
#     user.profile.save()

# @receiver(user_logged_out)
# def got_offline(sender, user, request, **kwargs):
#     user.profile.is_online = False
#     user.profile.save()


class SignUpView(CreateView):
    '''
    Sign up view
    """'''

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
