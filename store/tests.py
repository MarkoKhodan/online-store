from django.test import TestCase, Client

client = Client()


class TestUrl(TestCase):
    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>IPHONE 14</title>")
