# Generated by Django 3.2.3 on 2021-11-26 05:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('packeges', '0008_packageorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packageorder',
            name='id',
        ),
        migrations.AddField(
            model_name='packageorder',
            name='package_uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='packageorder',
            name='order_id',
            field=models.CharField(max_length=300, primary_key=True, serialize=False),
        ),
    ]
