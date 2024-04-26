from django.core import mail
from rest_framework import status
from rest_framework.test import APITestCase

class AccountsTestCase(APITestCase):

    register_url = "/api/auth/register/"
    verify_email_url = "/api/auth/register/verify-email/"
    login_url = "/api/auth/login/"

    def test_register(self):
        # register data
        data = {
            "email": "user@example-email.com",
            "password1": "verysecret",
            "password2": "verysecret",
        }
        # send POST request to "/api/auth/register/"
        response = self.client.post(self.register_url, data)
        # check the response status and data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["detail"], "Verification e-mail sent.")
