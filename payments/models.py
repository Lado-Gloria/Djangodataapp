from django.db import models

class Payments(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ("Cash", "Cash"),
        ("Credit Card", "Credit Card"),
        ("M pesa", "M pesa"),
    )
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_time = models.TimeField()
    payment_date = models.DateField()
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.name