# Generated by Django 3.1.3 on 2021-01-04 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_auto_20210104_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule_mod',
            name='sunday',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
