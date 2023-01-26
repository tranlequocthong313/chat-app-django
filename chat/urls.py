from django.urls import path
from .views import ChatJoinView, ChatRoomView, create_room, search_room

urlpatterns = [
    path(
        "room",
        create_room,
        name="chat_create",
    ),
    path(
        "rooms",
        ChatJoinView.as_view(),
        name="chat_join",
    ),
    path(
        "rooms/<int:pk>/join",
        ChatRoomView.as_view(),
        name="chat_room",
    ),
]
