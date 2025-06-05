from django.test import TestCase
from django.contrib.auth.models import User

from .models import UserProfile


class ProfileModelTests(TestCase):
    def test_profile_created_on_user_creation(self):
        user = User.objects.create_user(username="tester")
        self.assertTrue(UserProfile.objects.filter(user=user).exists())
        profile = UserProfile.objects.get(user=user)
        self.assertEqual(str(profile), "tester")
