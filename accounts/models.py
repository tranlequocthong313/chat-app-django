from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Customize default user model from django's auth app
    """

    email = models.EmailField(max_length=100, null=True, blank=True)
    avatar = models.URLField(
        null=True,
        blank=True,
        default="https://thumbs.dreamstime.com/b/default-avatar-profile-vector-user-profile-default-avatar-profile-vector-user-profile-profile-179376714.jpg",
    )
