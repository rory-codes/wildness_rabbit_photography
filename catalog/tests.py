from django.test import TestCase
from django.urls import reverse

class CatalogSmokeTests(TestCase):
    def test_home_ok(self):
        resp = self.client.get(reverse("catalog:home"))
        self.assertEqual(resp.status_code, 200)