from django.test import TestCase
from django.urls import reverse

from products.models import Product, Category


class BagViewsTests(TestCase):
    def setUp(self):
        category = Category.objects.create(name="snack")
        self.product = Product.objects.create(name="Chips", description="crispy", price=1, category=category)

    def test_add_adjust_and_remove_bag(self):
        add_url = reverse("add_to_bag", args=[self.product.id])
        adjust_url = reverse("adjust_bag", args=[self.product.id])
        remove_url = reverse("remove_from_bag", args=[self.product.id])

        # add
        response = self.client.post(add_url, {"quantity": 2, "redirect_url": reverse("products")})
        self.assertEqual(self.client.session["bag"].get(str(self.product.id)), 2)
        self.assertEqual(response.status_code, 302)

        # adjust
        response = self.client.post(adjust_url, {"quantity": 1})
        self.assertEqual(self.client.session["bag"].get(str(self.product.id)), 1)
        self.assertEqual(response.status_code, 302)

        # remove
        response = self.client.post(remove_url)
        self.assertNotIn(str(self.product.id), self.client.session.get("bag", {}))
        self.assertEqual(response.status_code, 200)

    def test_view_bag_template(self):
        url = reverse("view_bag")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bag/bag.html")

    def test_bag_contents_context(self):
        add_url = reverse("add_to_bag", args=[self.product.id])
        self.client.post(add_url, {"quantity": 3, "redirect_url": reverse("products")})
        from bag.contexts import bag_contents
        request = self.client.get(reverse("view_bag")).wsgi_request
        context = bag_contents(request)
        self.assertEqual(context["product_count"], 3)
        self.assertTrue(context["bag_items"])
