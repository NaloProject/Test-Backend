from django.db import IntegrityError
from django.test import TestCase

from icecream_api.models.item_related import Batch, Item

# Create your tests here.


class BatchTestCase(TestCase):
    def setUp(self):
        Item.objects.create(name="item1", price=2)
        choco = Item.objects.get(name="item1")
        Batch.objects.create(name="Batch1", stock=40, item=choco)

    def test_Batch(self):
        choco = Batch.objects.get(name="Batch1")
        self.assertEqual(choco.item.name, "item1")
        self.assertEqual(choco.stock, 40)
        self.assertEqual(choco.name, "Batch1")

    def test_get_Batch(self):
        choco = Batch.objects.get(name="Batch1")
        self.assertEqual(choco.stock, 40)
        choco.get(10)
        self.assertEqual(choco.stock, 30)

    def test_refill_Batch(self):
        choco = Batch.objects.get(name="Batch1")
        self.assertEqual(choco.stock, 40)
        choco.get(10)
        choco.refill(10)
        self.assertEqual(choco.stock, 40)

    def test_is_available(self):
        choco = Batch.objects.get(name="Batch1")
        self.assertEqual(choco.stock, 40)
        self.assertTrue(choco.is_available(10))
        self.assertFalse(choco.is_available(50))
