from datetime import datetime
from djongo import models
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)


class ItemProperties(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(null=True, blank=True, default=None)
    brand = models.CharField(max_length=100, null=True, blank=True, default=None)
    expiry_date = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True


class ShoppingList(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    quantity = models.PositiveIntegerField()
    item = models.EmbeddedField(model_container=ItemProperties)
