# Generated by Django 4.1.1 on 2022-12-15 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_customerorder_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='order_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='orders.orderstatus'),
        ),
    ]