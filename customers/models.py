from django.db import models
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=32)
    contact =models.BigIntegerField()
    email =models.CharField(max_length=32)
    password = models.CharField(max_length=32)
def __stri__(self):
    return self.name