# Generated by Django 3.2.3 on 2021-11-28 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packeges', '0010_package_accomodation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packageorder',
            name='contact_no',
            field=models.CharField(max_length=14),
        ),
    ]
