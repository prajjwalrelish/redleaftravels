# Generated by Django 3.2.3 on 2021-12-13 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packeges', '0021_alter_packageorder_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packageorder',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]