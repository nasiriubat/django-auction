# Generated by Django 3.2.3 on 2021-05-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210520_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
