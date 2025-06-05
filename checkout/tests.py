from django.test import TestCase

from products.models import Product, Category
from .models import Order, OrderLineItem


class OrderModelTests(TestCase):
    def setUp(self):
        category = Category.objects.create(name="drink")
        self.product = Product.objects.create(name="Water", description="clear", price=1, category=category)

    def test_order_number_generated(self):
        order = Order.objects.create(
            full_name="Tester",
            email="test@example.com",
            phone_number="1234",
            country="US",
            town_or_city="Town",
            street_address1="Street",
        )
        self.assertTrue(order.order_number)
        self.assertEqual(len(order.order_number), 32)

    def test_order_lineitem_updates_total(self):
        order = Order.objects.create(
            full_name="Tester",
            email="t@example.com",
            phone_number="1234",
            country="US",
            town_or_city="Town",
            street_address1="Street",
        )
        OrderLineItem.objects.create(order=order, product=self.product, quantity=2)
        order.refresh_from_db()
        expected_total = self.product.price * 2
        self.assertEqual(order.order_total, expected_total)
        self.assertEqual(order.grand_total, expected_total if expected_total >= 50 else expected_total + order.delivery_cost)
