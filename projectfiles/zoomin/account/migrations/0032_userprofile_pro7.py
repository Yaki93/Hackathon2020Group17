# Generated by Django 3.1.3 on 2021-01-06 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0031_auto_20210106_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='pro7',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
