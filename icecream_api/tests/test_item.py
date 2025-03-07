from django.test import TestCase

from icecream_api.models.item_related import Item

# Create your tests here.


class ItemTestCase(TestCase):
    def setUp(self):
        Item.objects.create(name="item1", price=2)
        Item.objects.create(name="item2", price=2)

    def test_item(self):
        choco = Item.objects.get(name="item1")
        self.assertEqual(choco.price, 2)
        self.assertEqual(choco.name, "item1")
