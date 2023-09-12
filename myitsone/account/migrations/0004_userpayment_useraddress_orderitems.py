# Generated by Django 4.2.4 on 2023-09-03 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_cart'),
        ('account', '0003_orderdetail_note_alter_orderdetail_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(max_length=254)),
                ('payment_provider', models.CharField(max_length=254)),
                ('account_no', models.CharField(max_length=254)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_address', models.CharField(max_length=254)),
                ('ward', models.CharField(max_length=254)),
                ('city', models.CharField(max_length=254)),
                ('special_instruction', models.CharField(blank=True, max_length=254)),
                ('contactPhone', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.orderdetail')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.products')),
            ],
        ),
    ]
