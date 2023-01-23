from django.test import TestCase
from django.utils import timezone

from accounts.models import CustomUser as User
from passwords.models import Password
from websites.models import Website

from hashlib import sha256


class PasswordTests(TestCase):

    def setUp(self):
        user = User.objects.create(
            username = 'testusername',
            first_name = 'testfirstname',
            last_name = 'testlastname',
            email = 'testusername@test.com',
        )
        website = Website.objects.create(
            name = 'A Test Website',
            url = 'https://www.websitefortesting.com/',
            description = 'A sample website for testing purposes',
        )
        Password.objects.create(
            account = user,
            username = user.username, # could be other username
            password_hash = sha256('test-password'.encode('utf-8')).hexdigest(),
            website = website,
        )

    def test_password_model(self):
        password = Password.objects.get(account=User.objects.get(username='testusername'))
        self.assertEqual(password.username, 'testusername')
        self.assertEqual(password.password_hash, sha256('test-password'.encode('utf-8')).hexdigest())
        self.assertEqual(password.website, Website.objects.get(url='https://www.websitefortesting.com/'))
        self.assertEqual(password.added_on.timetuple()[:3], timezone.now().timetuple()[:3])