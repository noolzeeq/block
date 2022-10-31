# Generated by Django 2.0 on 2022-10-31 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('type', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('shipment_date', models.DateField()),
                ('shipping_date', models.DateField()),
                ('status', models.IntegerField(null=True)),
            ],
        ),
    ]