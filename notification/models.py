from django.db import models
# Create your models here.
class Notification(models.Model):
    name = models.CharField(max_length=32)
    contact =models.BigIntegerField()
    message =models.CharField(max_length=32)
def __stri__(self):
    return self.name