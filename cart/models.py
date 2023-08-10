from django.db import models
# Create your models here.


class Cart(models.Model):
    delivery_method = models.CharField(max_length=15)
    number_of_products = models.IntegerField()
    products_total = models.DecimalField(max_digits=6, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=6, decimal_places=2)
    payment_method = models.CharField(max_length = 15)
    def __str__(self):
        return self.delivery_method