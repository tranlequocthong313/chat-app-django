from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Message, Room


test_user = get_user_model()


class CreateRoomTests(TestCase):
    """
    Create new room test
    """

    room_name = "testroom"
    email = "test@gmail.com"
    password = "password"

    def setUp(self) -> None:
        self.room = Room.objects.create(name=self.room_name)
        mem1 = self.create_user("testuser1")
        mem2 = self.create_user("testuser2")
        mem3 = self.create_user("testuser3")
        self.members = [mem1.id, mem2.id, mem3.id]
        self.room.members.add(*self.members)
        self.client.force_login(mem1)

    def create_user(self, username):
        """
        Create user for testing
        """
        return get_user_model().objects.create_user(  # type: ignore
            username=username, email=self.email, password=self.password
        )

    def test_string_representation(self):
        """
        Test __str__ method in model
        """
        self.assertEqual(str(self.room), self.room_name)

    def test_get_absolute_url(self):  # new
        """
        Test absolute url
        """
        self.assertEqual(self.room.get_absolute_url(), "/chat/chat_room/1")

    def test_new_room_data(self):
        """
        Test room's data
        """
        self.assertEqual(f"{self.room.name}", self.room_name)
        self.assertEqual(self.room.members.count(), len(self.members))
        self.assertEqual(Room.objects.all().count(), 1)

    def test_create_new_room_by_http_request(self):
        """
        Test creating new room by http request
        """

        success_response = self.client.post(
            reverse("chat_create"), {"room-name": self.room_name}
        )
        fail_response = self.client.post(reverse("chat_create"), {"room-name": ""})
        self.assertEqual(success_response.status_code, 302)
        self.assertEqual(fail_response.status_code, 500)
        self.assertRedirects(success_response, "/chat/chat_room/2", 302, 200)
        self.assertRedirects(
            success_response, reverse("chat_room", args=[str(2)]), 302, 200
        )
        self.assertEqual(Room.objects.all().count(), 2)
        self.assertEqual(Room.objects.all()[1].name, self.room_name)
        self.assertEqual(Room.objects.all()[1].members.count(), 1)


class JoinChatRoomViewTests(TestCase):
    """
    Test chat join page page view and logics
    """

    room_name = "testroom"

    def setUp(self) -> None:
        self.room = Room.objects.create(name=self.room_name)

    def test_join_page_status_code(self):
        """
        Test getting 200 status code when get url
        """
        response = self.client.get("/chat/join_room/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        """
        Test getting 200 status code when get url pattern name
        """
        response = self.client.get(reverse("chat_join"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test using correct template
        """
        response = self.client.get(reverse("chat_join"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "chat_join.html")

    def test_search_room_by_name(self):
        """
        Test searching room chat by name
        """
        success_response = self.client.post(
            reverse("search_room"),
            {"room-name": self.room_name},
        )
        fail_response = self.client.post(
            reverse("search_room"),
            {"room-name": "fail"},
        )
        self.assertEqual(success_response.status_code, 200)
        self.assertTemplateUsed(success_response, "chat_join.html")
        self.assertEqual(success_response.context["rooms"][0].name, self.room_name)
        self.assertContains(success_response, self.room_name)
        self.assertEqual(fail_response.status_code, 404)

    def test_room_list_view(self):
        """
        Test room's view if contains the same data
        of object was created
        """
        response = self.client.get(reverse("chat_join"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.room_name)
        self.assertTemplateUsed(response, "chat_join.html")


class ChatRoomTests(TestCase):
    """
    Chat room tests
    """

    room_name = "testroom"

    def setUp(self):
        self.room = Room.objects.create(name=self.room_name)
        self.user = get_user_model().objects.create(
            username="testuser", password="password"
        )

        self.message = Message.objects.create(
            content="testmessage",
            author=self.user,
            room_id=self.room.id,
        )
        self.client.force_login(self.user)

    def test_view_status_code(self):
        """
        Test view status code
        """
        url_resp = self.client.get("/chat/chat_room/1")
        self.assertEqual(url_resp.status_code, 200)
        name_resp = self.client.get(reverse("chat_room", args=[str(1)]))
        self.assertEqual(name_resp.status_code, 200)

    def test_view_used_template(self):
        """
        Test view used template
        """
        resp = self.client.get(reverse("chat_room", args=[str(1)]))
        self.assertTemplateUsed(resp, "chat_room.html")

    def test_view_contains_texts(self):
        """
        Test view contains texts
        """
        resp = self.client.get(reverse("chat_room", args=[str(1)]))
        self.assertContains(resp, self.room_name)
        self.assertContains(resp, self.message.content)
        self.assertContains(resp, self.room.members.count())


class MessageTests(TestCase):
    """
    Message tests
    """

    content = "test"
    username = "testuser"
    room_name = "testroom"

    def setUp(self):
        self.message = Message.objects.create(
            content=self.content,
            author=get_user_model().objects.create(
                username=self.username, password="password"
            ),
            room=Room.objects.create(name=self.room_name),
        )

    def test_string_representation(self):
        """
        Test __str__
        """
        self.assertEqual(str(self.message), self.message.content)

    def test_message_data(self):
        """
        Test message's data
        """
        self.assertEqual(self.message.content, self.content)
        self.assertEqual(self.message.author.username, self.username)
        self.assertEqual(self.message.room.name, self.room_name)
