from django.urls import path
from django.views.generic import TemplateView
from .views import ChatJoinView, ChatRoomView, create_room, search_room

urlpatterns = [
    path("", TemplateView.as_view(template_name="chat_home.html"), name="chat_home"),
    path(
        "create_room/",
        create_room,
        name="chat_create",
    ),
    path(
        "join_room/",
        ChatJoinView.as_view(),
        name="chat_join",
    ),
    path(
        "chat_room/<int:pk>",
        ChatRoomView.as_view(),
        name="chat_room",
    ),
    path(
        "search_room/",
        search_room,
        name="search_room",
    ),
]
