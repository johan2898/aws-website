# Generated by Django 2.1.5 on 2020-12-02 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20201118_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='telling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField(max_length=1000)),
            ],
        ),
    ]
