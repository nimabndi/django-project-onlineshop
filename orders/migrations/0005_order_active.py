# Generated by Django 4.0.1 on 2022-01-31 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_orderitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
