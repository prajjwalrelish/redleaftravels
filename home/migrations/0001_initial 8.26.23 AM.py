# Generated by Django 3.2.5 on 2021-11-30 02:34

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('packeges', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('author', models.CharField(default='divyanshu soni', max_length=50)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='blogs/images')),
            ],
        ),
        migrations.CreateModel(
            name='clientReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('name', models.CharField(max_length=50)),
                ('review', models.TextField()),
                ('address', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(default='', upload_to='client_reviews/images')),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('responded', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Specialoffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.IntegerField(default=1)),
                ('price', models.IntegerField(default=0)),
                ('discount', models.IntegerField()),
                ('desc', models.TextField(default='')),
                ('is_active', models.BooleanField(default=True)),
                ('package', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='packeges.package')),
            ],
        ),
    ]
