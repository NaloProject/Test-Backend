import uuid
from django.db import models
from icecream_api.models.item_related import Batch, Item


class Command(models.Model):
    identifier = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    items_needed = models.JSONField(default=dict())
    status = models.BooleanField(default=False)
    price = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def prepare(self) -> bool:
        items_needed = self.items_needed
        _allocation = set()
        for key in items_needed:
            batch = Batch.objects.get(name=key)
            if batch.is_available(int(items_needed[key])):
                item = Item.objects.get(name=key)
                self.price += float(item.price) * int(items_needed[key])
                batch.get(int(items_needed[key]))
                _allocation.add(key)
            else:
                print(f"Email to Admin User - in need of a refill for {key}")
                self.cancel(_allocation)
                return False

        self.status = True
        self.save()
        return self.status

    def get_information(self) -> dict:
        return {"identifier": str(self.identifier), "price": str(self.price)}

    def cancel(self, _allocation: set) -> None:
        self.price = 0.0
        for key in _allocation:
            batch = Batch.objects.get(name=key)
            batch.refill(int(self.items_needed[key]))
            batch.save()
        self.save()
