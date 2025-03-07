import uuid

from django.test import TestCase

from icecream_api.models.command_related import Command
from icecream_api.models.item_related import Batch, Item


class CommandTestCase(TestCase):
    def setUp(self):
        Item.objects.create(name="choco", price=2)
        Item.objects.create(name="cake", price=2)
        Batch.objects.create(
            name="choco", stock=40, item=Item.objects.get(name="choco")
        )
        Batch.objects.create(name="cake", stock=40, item=Item.objects.get(name="cake"))

    def test_command(self):
        reference = uuid.uuid4()
        command = Command.objects.create(
            identifier=reference, items_needed={"choco": "10"}
        )
        command.prepare()
        ref = command.get_information()["identifier"]
        self.assertEqual(Batch.objects.get(name="choco").stock, 30)
        self.assertEqual(ref, str(reference))

    def test_command_multiple(self):
        reference = uuid.uuid4()
        Command.objects.create(
            identifier=reference, items_needed={"choco": "10", "cake": "5"}
        ).prepare()
        self.assertEqual(Batch.objects.get(name="choco").stock, 30)
        self.assertEqual(Batch.objects.get(name="cake").stock, 35)

    def test_command_fail(self):
        Command.objects.create(
            identifier=uuid.uuid4(), items_needed={"choco": "40", "cake": "5"}
        ).prepare()
        self.assertEqual(Batch.objects.get(name="choco").stock, 0)
        self.assertEqual(Batch.objects.get(name="cake").stock, 35)
        command = Command.objects.create(
            identifier=uuid.uuid4(), items_needed={"choco": "5", "cake": "5"}
        )
        self.assertFalse(command.prepare())

        self.assertEqual(Batch.objects.get(name="choco").stock, 0)
        self.assertEqual(Batch.objects.get(name="cake").stock, 35)
