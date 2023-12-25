from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title='Ice Cream', price=80, inventory=100, category_id=5)
        self.assertEqual(item, 'Ice Cream : 80')
        
class MenuItemsViewTest(TestCase):
    def test_getall(self):
        getall = MenuItem.objects.setup(title='FuFu & Egusi', price=25.45, inventory=150, category_id=3) 
        self.assertEqual(getall, 'FuFu & egusi : 25.45')       