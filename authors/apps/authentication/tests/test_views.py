from django.urls import reverse

from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from ..models import User


class BaseViewTest(APITestCase):
    client = APIClient()

    def setUp(self):
        # create super user
        self.user = User.objects.create_superuser(
            username="test_user",
            email="test@mail.com",
            password="testing",
        )

class LoginUserTest(BaseViewTest):
    def test_login_user_with_correct_details(self):
        url = reverse("login", kwargs={"version": "v1"})
        params = {
            "email":"test@mail.com",
             "password": "testing"
             }
        response = self.client.post(url, params)
        self.assertEqual(response.data['email'], "test@mail.com")
