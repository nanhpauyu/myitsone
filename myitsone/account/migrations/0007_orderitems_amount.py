# Generated by Django 4.2.4 on 2023-09-03 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_rename_order_id_orderitems_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='amount',
            field=models.IntegerField(null=True),
        ),
    ]
