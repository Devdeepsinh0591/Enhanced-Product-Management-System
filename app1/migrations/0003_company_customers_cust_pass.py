# Generated by Django 3.1.7 on 2021-06-12 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_company_customers'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_customers',
            name='cust_pass',
            field=models.CharField(default='', max_length=200),
        ),
    ]
