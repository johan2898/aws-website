# Generated by Django 2.1.5 on 2020-11-18 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201111_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='stories',
            name='data',
            field=models.TextField(default=''),
        ),
    ]
