from django.db import models
from django.db.models import ForeignKey
from django.utils.translation.trans_real import catalog


class Item(models.Model):
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    standard_price = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.CharField(blank=True, max_length=500)
    catalog_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.name} {self.catalog_number}"

class ItemSpecification(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="properties")
    height_mm = models.DecimalField(decimal_places=2, max_digits=6)
    width_mm = models.DecimalField(decimal_places=2, max_digits=6)
    depth_mm = models.DecimalField(decimal_places=2, max_digits=6)
    weight_kg = models.DecimalField(decimal_places=3, max_digits=6)

    def __str__(self):
        return f"{self.item.name} - {self.weight_kg} {self.height_mm}x{self.width_mm}x{self.depth_mm}"