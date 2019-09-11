from django.db import models


class Order(models.Model):
    description = models.TextField()
    price = models.IntegerField()

