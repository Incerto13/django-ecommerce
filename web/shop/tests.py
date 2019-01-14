from django.test import TestCase
from django.urls import reverse

from .models import Category, Product

from django.contrib.auth.models import User


class IndexPageTests(TestCase):

    def test_index_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('shop:product_list'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('shop:product_list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product/list.html')


class CategoryAndProductTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        category = Category.objects.create(name='Test_cat')
        Product.objects.create(name='Test_prod', category=category)
