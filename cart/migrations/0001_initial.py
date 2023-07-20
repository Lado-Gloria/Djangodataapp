# Generated by Django 4.2.3 on 2023-07-15 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_method', models.CharField(max_length=15)),
                ('number_of_products', models.IntegerField()),
                ('products_total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('shipping_cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('payment_method', models.CharField(max_length=15)),
            ],
        ),
    ]