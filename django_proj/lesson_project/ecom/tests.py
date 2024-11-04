from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from ecom.models import Profile
from rest_framework import status
# Create your tests here.

class ProfileAPITests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(username="test", password="test")
        self.client.force_authenticate(user=self.user)
        self.profile_url = "/api/profiles/"

    def test_list_profiles_authenticated(self):
        profile = Profile.objects.create(user_id=self.user, address='test')

        response = self.client.get(self.profile_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["address"], profile.address)

    def test_create_profile_authenticated(self):
        data = {
            "address": "test",
            "user_id": self.user.id
        }

        response = self.client.post(self.profile_url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)

    def test_get_profile_by_pk(self):
        profile = Profile.objects.create(user_id=self.user, address='test')

        response = self.client.get(self.profile_url + str(profile.pk) + "/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["address"], profile.address)

