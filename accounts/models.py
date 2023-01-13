from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Customize default user model from django's auth app
    """

    birth_date = models.DateTimeField(null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    avatar = models.URLField(
        null=True,
        blank=True,
        default="https://thumbs.dreamstime.com/b/default-avatar-profile-vector-user-profile-default-avatar-profile-vector-user-profile-profile-179376714.jpg",
    )
    accept_stranger_message = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)
    friends = models.ManyToManyField("CustomUser", blank=True)


# TODO: Creating this model for friend features
class FriendRequest(models.Model):
    """
    Friend Request
    """

    from_user = models.ForeignKey(
        "CustomUser", related_name="from_user", on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        "CustomUser", related_name="to_user", on_delete=models.CASCADE
    )
