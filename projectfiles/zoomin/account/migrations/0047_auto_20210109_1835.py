# Generated by Django 3.1.3 on 2021-01-09 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0046_auto_20210109_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board_class',
            name='publication_date',
            field=models.DateField(default='2021-01-09', verbose_name='תאריך'),
        ),
    ]
