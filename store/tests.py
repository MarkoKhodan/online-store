from django.test import TestCase, Client

client = Client()


class TestUrl(TestCase):
    fixtures = ["item.json", ]

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "IPHONE 14")

    def test_sale_page(self):
        response = self.client.get("/sale/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "IPHONE 14")

        response = self.client.get("/sale/2/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "MacBook Pro")


