from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status

from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        
        self.pizza = MenuItem.objects.create(title='Pizza', price=12.99, inventory=10)
        self.burger = MenuItem.objects.create(title='Burger', price=8.99, inventory=5)
        self.pasta = MenuItem.objects.create(title='Pasta', price=15.99, inventory=7)
    
    def loginAsTestUser(self) -> None:
        self.client.login(username='testuser', password='testpassword')
    
    def test_view_authentication(self) -> None:
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.loginAsTestUser()
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_getall(self):
        self.loginAsTestUser()
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        menu = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)