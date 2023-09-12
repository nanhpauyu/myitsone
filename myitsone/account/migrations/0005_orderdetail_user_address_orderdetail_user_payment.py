# Generated by Django 4.2.4 on 2023-09-03 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_userpayment_useraddress_orderitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='user_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.useraddress'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='user_payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.userpayment'),
        ),
    ]
