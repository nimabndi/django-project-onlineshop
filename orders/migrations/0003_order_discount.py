# Generated by Django 4.0.1 on 2022-01-31 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]