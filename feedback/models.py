from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=300)
    location=models.CharField(max_length=200)
    messages =models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return self.name
    


