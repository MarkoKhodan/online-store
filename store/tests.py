from django.test import TestCase, Client

client = Client()


class TestUrl(TestCase):
    fixtures = ["item.json"]

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h2> IPHONE 14 </h2>")
