# Generated by Django 4.1.1 on 2022-12-15 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_customerorder_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='order_status',
            field=models.ForeignKey(default='NEW', on_delete=django.db.models.deletion.RESTRICT, to='orders.orderstatus'),
        ),
    ]
