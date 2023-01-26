from datetime import datetime
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
class SignupPageTests(TestCase):
    """
    Test signup page view and logics
    """

    username = "newuser"
    email = "newuser@email.com"
    avatar = "avatar"

    def test_signup_page_status_code(self):
        """
        Test getting 200 status code when get url
        """
        response = self.client.get("/account/signup")
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        """
        Test getting 200 status code when get url pattern name
        """
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test using correct template
        """
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        """
        Test signup form
        """
        get_user_model().objects.create_user(  # type: ignore
            self.username,
            self.email,
            avatar=self.avatar,
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)  # type: ignore
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)  # type: ignore
        self.assertEqual(get_user_model().objects.all()[0].avatar, self.avatar)  # type: ignore
