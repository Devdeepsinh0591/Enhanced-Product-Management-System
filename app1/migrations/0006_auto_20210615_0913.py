# Generated by Django 3.1.7 on 2021-06-15 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_customer_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_order',
            name='status',
            field=models.CharField(default='False', max_length=200),
        ),
    ]
