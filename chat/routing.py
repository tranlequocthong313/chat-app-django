# This file is corresponding with 'urls.py' of Django
from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [re_path(r"ws/socket-server/", ChatConsumer.as_asgi())]
