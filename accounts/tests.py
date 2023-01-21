from django.test import TestCase
from django.utils import timezone

from accounts.models import CustomUser as User


class UserTests(TestCase):

    def setUp(self):
        User.objects.create(
            username = 'testusername',
            first_name = 'testfirstname',
            last_name = 'testlastname',
            email = 'testusername@test.com',
        )

    def test_user_model(self):
        testuser = User.objects.get(username='testusername')
        self.assertEqual(testuser.first_name, 'testfirstname')
        self.assertEqual(testuser.last_name, 'testlastname')
        self.assertEqual(testuser.email, 'testusername@test.com')
        self.assertEqual(testuser.is_staff, False)
        self.assertEqual(testuser.is_active, True)
        self.assertEqual(testuser.date_joined.timetuple()[:3], timezone.now().timetuple()[:3])