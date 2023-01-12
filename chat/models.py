from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.
class Message(models.Model):
    """
    This model handles messages will be sent in this app.
    """

    content = models.TextField(max_length=500)
    send_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="messages"
    )
    chat_room = models.ForeignKey(
        "Room", on_delete=models.CASCADE, related_name="messages"
    )

    def __str__(self) -> str:
        return self.content[:50]


class Room(models.Model):
    """
    Chat room contains messages were sent
    """

    members = models.ManyToManyField(get_user_model())
    name = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        """
        Get absolute url after creating success.
        """
        return reverse("chat_room", args=[str(self.id)])
