# Generated by Django 4.2.5 on 2023-09-17 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_transaction_is_returned'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_id',
            field=models.IntegerField(default=1),
        ),
    ]
