# Generated by Django 3.1.3 on 2021-01-09 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0045_auto_20210109_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_schedule',
            name='end_time',
            field=models.TimeField(null=True, verbose_name='שעת סיום'),
        ),
        migrations.AlterField(
            model_name='test_schedule',
            name='start_time',
            field=models.TimeField(null=True, verbose_name='שעת התחלה'),
        ),
    ]
