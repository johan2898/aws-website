# Generated by Django 2.1.4 on 2020-11-03 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_title', models.CharField(max_length=200)),
                ('story_description', models.TextField()),
                ('story_published', models.DateTimeField(verbose_name='Date Published')),
            ],
        ),
    ]
