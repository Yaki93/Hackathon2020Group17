# Generated by Django 3.1.3 on 2021-01-09 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0039_remove_userprofile_email_rec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_schedule',
            name='date',
            field=models.DateField(blank=True, default='2021-01-09', null=True, verbose_name='תאאריך'),
        ),
    ]
