# Generated by Django 3.2.3 on 2021-11-29 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_clientreview_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(default='divyanshu soni', max_length=50),
        ),
    ]
