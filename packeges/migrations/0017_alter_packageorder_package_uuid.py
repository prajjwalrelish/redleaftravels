# Generated by Django 3.2.3 on 2021-12-12 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packeges', '0016_auto_20211212_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packageorder',
            name='package_uuid',
            field=models.CharField(max_length=100),
        ),
    ]