# Generated by Django 3.1.3 on 2021-01-04 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20210104_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule_mod',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]