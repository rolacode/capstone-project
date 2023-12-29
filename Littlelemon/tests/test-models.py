from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title='Ice Cream', price=80, inventory=100, category_id=5)
        self.assertEqual(item, 'Ice Cream : 80')
        
class MenuItemsViewTest(TestCase):
    def setup(self):
        getall = MenuItem.objects.test_getall(title='FuFu & Egusi', price=85.45, inventory=150, category_id=3) 
        self.assertEqual(getall, 'FuFu & egusi : 85.45')       