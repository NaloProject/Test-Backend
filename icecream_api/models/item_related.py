from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Batch(models.Model):
    name = models.CharField(max_length=50, default=None)
    stock = models.IntegerField(default=None)
    max_stock = models.IntegerField(default=40)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False, default=None)

    def __str__(self) -> str:
        return self.name

    def get(self, nb_items: int) -> None:
        self.stock -= nb_items
        self.save()

    def refill(self, nb_items: int = 0, full=False) -> None:
        if full:
            self.stock = self.max_stock
        else:
            self.stock += nb_items
            if self.stock > self.max_stock:
                self.stock = self.max_stock
        self.save()

    def is_available(self, nb_items: int) -> bool:
        return self.stock >= nb_items
