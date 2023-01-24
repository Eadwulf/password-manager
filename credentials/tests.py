from django.test import TestCase
from django.utils import timezone

from accounts.models import User as User
from credentials.models import Credential

from hashlib import sha256


class PasswordTests(TestCase):

    def setUp(self):
        user = User.objects.create(
            username = 'testusername',
            first_name = 'testfirstname',
            last_name = 'testlastname',
            email = 'testusername@test.com',
        )
        Credential.objects.create(
            user = user,
            username = user.username, # could be other username
            password = sha256('test-password'.encode('utf-8')).hexdigest(),
        )

    def test_credential_model(self):
        credentials = Credential.objects.get(account=User.objects.get(username='testusername'))
        self.assertEqual(credentials.username, 'testusername')
        self.assertEqual(credentials.password, sha256('test-password'.encode('utf-8')).hexdigest())
        self.assertEqual(credentials.added_on.timetuple()[:3], timezone.now().timetuple()[:3])