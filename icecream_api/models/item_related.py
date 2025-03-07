from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Batch(models.Model):
    name = models.CharField(max_length=50, default=None)
    stock = models.IntegerField(default=None)
    max_stock = models.IntegerField(default=40)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False, default=None)

    def __str__(self):
        return self.name

    def get(self, nb_items: int):
        """Réduit le stock de boules pour ce parfum et vérifie que cela est possible."""
        self.stock -= nb_items
        self.save()

    def refill(self, nb_items: int = 0, full=False):
        """Reconstitue le stock à une certaine quantité."""
        if full:
            self.stock = self.max_stock
        else:
            self.stock += nb_items
            if self.stock > self.max_stock:
                self.stock = self.max_stock
        self.save()

    def is_available(self, nb_items: int) -> bool:
        """Retourne True si le parfum est en stock pour le nombre de boules demandé."""
        return self.stock >= nb_items
