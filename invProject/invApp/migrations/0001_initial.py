# Generated by Django 5.1 on 2024-08-29 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('stock_keep_unit', models.CharField(max_length=50, unique=True)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('supplier', models.CharField(max_length=100)),
            ],
        ),
    ]
