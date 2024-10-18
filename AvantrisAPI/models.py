# models.py
from django.db import models

class Item(models.Model):
    item_id = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()

class User(models.Model):
    user_id = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Item)

