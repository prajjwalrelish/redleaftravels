# Generated by Django 3.2.3 on 2021-11-25 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packeges', '0007_auto_20211118_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='packageOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('package_date', models.CharField(max_length=11)),
                ('adults', models.IntegerField()),
                ('childrens', models.IntegerField()),
            ],
        ),
    ]
