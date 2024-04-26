from django.test import TestCase

# Create your tests here.
class CustomUserTestCase(TestCase):
    def create_custom_user(self):
        page = self.client.get("/")
