# Generated by Django 3.2.3 on 2021-11-17 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packeges', '0004_package_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='image',
            field=models.ImageField(default=None, upload_to='packages/images'),
        ),
    ]
