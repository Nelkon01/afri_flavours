from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Product, Category, Allergen, Review


class ProductModelTests(TestCase):
    def test_category_str_and_friendly_name(self):
        category = Category.objects.create(name="meat", friendly_name="Meat")
        self.assertEqual(str(category), "meat")
        self.assertEqual(category.get_friendly_name(), "Meat")

    def test_product_and_allergen_str(self):
        category = Category.objects.create(name="fish")
        allergen = Allergen.objects.create(name="nuts")
        product = Product.objects.create(
            category=category,
            name="Tuna",
            description="Fresh tuna",
            price=10,
        )
        product.allergens.add(allergen)
        self.assertEqual(str(allergen), "nuts")
        self.assertEqual(str(product), "Tuna")

    def test_review_str(self):
        user = User.objects.create_user(username="tester")
        product = Product.objects.create(name="Yam", description="desc", price=5)
        review = Review.objects.create(product=product, user=user, text="Ok", rating=3)
        self.assertIn(user.username, str(review))
        self.assertIn(product.name, str(review))


class ProductViewsTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="veg")
        self.product = Product.objects.create(name="Carrot", description="desc", price=2, category=self.category)

    def test_all_products_view(self):
        url = reverse("products")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")
        self.assertIn(self.product, response.context["products"])

    def test_product_detail_view(self):
        url = reverse("product_detail", args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")
        self.assertEqual(response.context["product"], self.product)
