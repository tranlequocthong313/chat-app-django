from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Room


@require_http_methods(["POST"])
def create_room(request):
    """
    Create a new room with name
    """
    name = request.POST.get("room-name")
    if isinstance(name, str) and len(name) > 0:
        new_room = Room.objects.create(name=name)
        new_room.members.add(request.user)
        return redirect(new_room.get_absolute_url())
    else:
        return HttpResponse("Server Error!", status=500)


@require_http_methods(["POST"])
def search_room(request):
    """
    Search room with a full name or letters
    """
    name = request.POST.get("room-name")
    searched_rooms = Room.objects.filter(name__startswith=name)
    if searched_rooms:
        return render(request, "chat_join.html", {"rooms": searched_rooms})
    else:
        return HttpResponse("Not Found!", status=404)


class ChatJoinView(ListView):
    """
    Render current exist rooms view.
    """

    model = Room
    template_name = "chat_join.html"
    context_object_name = "rooms"


class ChatRoomView(LoginRequiredMixin, DetailView):
    """
    Render room with its id
    """

    model = Room
    template_name = "chat_room.html"
    context_object_name = "room"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        Room.objects.get(id=kwargs["object"].id).members.add(self.request.user.id)
        context["messages"] = list(self.serialize_messages(context["room"]))
        return context

    def serialize_messages(self, room):
        """
        Serialize messages in the room
        """
        for msg in room.messages.all()[:10]:
            local_dict = {}
            local_dict["content"] = msg.content
            local_dict["authorAvatar"] = msg.author.avatar
            local_dict["authorName"] = msg.author.username
            local_dict["sendDate"] = msg.send_date
            yield local_dict
