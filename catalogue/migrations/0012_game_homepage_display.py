# Generated by Django 2.2.6 on 2020-02-27 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0011_auto_20200225_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='homepage_display',
            field=models.BooleanField(default=False),
        ),
    ]
