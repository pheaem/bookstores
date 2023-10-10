# Generated by Django 4.2.5 on 2023-10-10 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='book',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='customer_detail',
        ),
        migrations.RemoveField(
            model_name='sale_report',
            name='book',
        ),
        migrations.RemoveField(
            model_name='sale_report',
            name='transaction',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='checkout',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Checkout',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Sale_Report',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
