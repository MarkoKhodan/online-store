from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase, Client
from decimal import *

from store.models import Item

client = Client()


class TestUrl(TestCase):

    fixtures = ["item.json", "initial_data.json"]

    def setUp(self) -> None:
        self.user = User.objects.get(id=1)
        self.client.force_login(self.user)

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "IPHONE 14")

    def test_sale_create_page(self):
        response = self.client.get("/sale/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "IPHONE 14")

        response = self.client.get("/sale/2/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "MacBook Pro")

    def test_sale_list_page(self):
        response = self.client.get("/sale/")
        self.assertEqual(response.status_code, 200)


class LoginRequiredTest(TestCase):
    def test_index(self):

        response = self.client.get("/sale/")

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/accounts/login/?next=/sale/")


class PaginationTest(TestCase):

    fixtures = [
        "employee.json",
        "item.json",
        "sale.json",
        "initial_data.json",
    ]

    def setUp(self) -> None:
        self.user = get_user_model().objects.get(id=1)
        self.client.force_login(self.user)

    def test_pagination_is_correct(self):
        response = self.client.get("/sale/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(len(response.context["sale_list"]) == 5)


class PriceChangesListTest(TestCase):

    fixtures = ["employee.json", "item.json", "sale.json", "initial_data.json"]

    def setUp(self) -> None:
        self.user = get_user_model().objects.get(id=1)
        self.client.force_login(self.user)
        self.client.post(
            "/admin/store/item/1/change/",
            {"title": "Test", "description": "Test descr", "price": 200},
        )

    def test_change_prices(self):

        item = Item.objects.create(title="title", description="description", price=200)
        item.price += 1
        item.save()
        item.save()
        self.client.post(
            f"/admin/store/item/{item.id}/change/",
            {"title": "Test", "description": "Test descr", "price": 300},
        )
        price_dynamics = list(
            item.price_changes.order_by("created_at").values_list(
                "new_price", flat=True
            )
        )
        self.assertListEqual(
            price_dynamics, [Decimal("200.00"), Decimal("201.00"), Decimal("300.00")]
        )
