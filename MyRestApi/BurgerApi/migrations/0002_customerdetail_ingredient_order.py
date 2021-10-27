# Generated by Django 3.1.2 on 2021-10-23 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliveryAddress', models.TextField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('paymentType', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salad', models.IntegerField(default=0)),
                ('cheese', models.IntegerField(default=0)),
                ('meat', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=20)),
                ('orderTime', models.CharField(max_length=100)),
                ('customer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='BurgerApi.customerdetail')),
                ('ingredients', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='BurgerApi.ingredient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
