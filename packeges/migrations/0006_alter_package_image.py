# Generated by Django 3.2.3 on 2021-11-18 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packeges', '0005_alter_package_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='image',
            field=models.ImageField(default='', upload_to='packages/images'),
        ),
    ]