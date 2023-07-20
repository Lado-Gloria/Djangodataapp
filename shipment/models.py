from django.db import models

# Create your models here.

class Shipment(models.Model):
     DELIVERY_CHOICES = [
        ('standard', 'Standard Delivery'),
        ('express', 'Express Delivery'),
        # Add more choices as needed
    ]
     name = models.CharField(max_length=255)
     orderName = models.CharField(max_length=300)
     orderTotal =models.IntegerField()
     location = models.CharField(max_length=200)
     deliveryType = models.CharField(max_length=10, choices=DELIVERY_CHOICES)
     totalcost =models.DecimalField(max_digits=10, decimal_places=2)
     status = models.BooleanField()
     date_created = models.DateTimeField(auto_now_add=True)
     date_updated = models.DateTimeField(auto_now=True)
     def __str__(self):
        return self.name
    






    