# Generated by Django 2.2 on 2020-03-12 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvShowsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='description',
            field=models.TextField(default='this is the default description'),
            preserve_default=False,
        ),
    ]
