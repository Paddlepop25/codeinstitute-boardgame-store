# Generated by Django 2.2.6 on 2020-01-31 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_auto_20200131_0320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='avavilable_stock',
            new_name='available',
        ),
        migrations.RemoveField(
            model_name='game',
            name='discount',
        ),
        migrations.AlterField(
            model_name='game',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='game',
            name='stock_left',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Discount',
        ),
    ]
