from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class HomePageViewTest(TestCase):
    """
    Test home page view
    """

    def test_view_url_exists_at_proper_location(self):
        """
        Test status code 200 if get correct url
        """
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        """
        Test status code 200 if get correct url by reverse its
        url pattern name
        """
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test using right template if get correct url by reverse its
        url pattern name
        """
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home.html")
