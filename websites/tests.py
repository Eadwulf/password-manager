from django.test import TestCase

from websites.models import Website


class WebsiteTests(TestCase):

    def setUp(self):
        Website.objects.create(
            name = 'A Test Website',
            url = 'https://www.websitefortesting.com/',
            description = 'A sample website for testing purposes',
        )

    def test_website_model(self):
        website = Website.objects.get(url='https://www.websitefortesting.com/')
        self.assertEqual(website.name, 'A Test Website')
        self.assertEqual(website.description, 'A sample website for testing purposes')
