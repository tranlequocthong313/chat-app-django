from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.

class Auth:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if self._access_auth_page_after_login(request ):
            return redirect(reverse('home'))                

        return response

    def _access_auth_page_after_login(self, request):
        path = request.path
        return ('login' in path or 'signup' in path) and request.user.is_authenticated
