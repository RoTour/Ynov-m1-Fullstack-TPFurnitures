from django.db import models

# Create your models here.


class ShopOwner(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)


class Shop(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    turnover = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(ShopOwner, on_delete=models.CASCADE, related_name='shops')


class Furniture(models.Model):
    CONDITION = {
        ('new', 'new'),
        ('used', 'used'),
        ('bad', 'bad'),
        ('broken', 'broken'),
    }
    STATUS = {
        ('available', 'Available'),
        ('sold', 'Sold'),
    }
    name = models.CharField(max_length=100)
    condition = models.CharField(max_length=10, choices=CONDITION, default='new')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS)
    location = models.ForeignKey(Shop, on_delete=models.PROTECT, related_name='furniture')

