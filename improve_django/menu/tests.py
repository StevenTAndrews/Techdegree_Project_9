from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import *


class MenuViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="Name", email="email@email.com", password="MyPassword")
        self.ingredient1 = Ingredient.objects.create(name="Meat",)
        self.ingredient2 = Ingredient.objects.create(name="Cheese",)
        self.ingredient3 = Ingredient.objects.create(name="Bacon",)
        self.item1 = Item.objects.create(
            name="Burger",
            description="A delicious burger.",
            chef=self.user,
            standard=True)
        self.item1.ingredients.set([self.ingredient1, self.ingredient2])
        self.item2 = Item.objects.create(
            name='Sandwich',
            description='A somewhat good sandwich.',
            chef=self.user,
            standard=True)
        self.item2.ingredients.set([self.ingredient2, self.ingredient3])
        self.menu = Menu.objects.create(season="Now")
        self.menu.items.set([self.item1])


    def test_menu_list_view(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_menu_detail(self):
        resp = self.client.get(reverse('menu_detail',kwargs={'pk': self.menu.pk}))
        self.assertEqual(resp.status_code, 200)

    def test_menu_create(self):
        resp = self.client.get('/')
        self.assertIn(self.menu, resp.context['menus'])