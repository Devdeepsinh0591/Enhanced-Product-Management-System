# Generated by Django 3.1.7 on 2021-06-14 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_company_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=0)),
                ('tot_price', models.PositiveIntegerField(default=0)),
                ('order_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('comp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company_details')),
                ('cust', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company_customers')),
                ('prod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.company_product')),
            ],
        ),
    ]
