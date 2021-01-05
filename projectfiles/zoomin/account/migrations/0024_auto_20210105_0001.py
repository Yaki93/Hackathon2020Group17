# Generated by Django 3.1.3 on 2021-01-04 22:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_auto_20210104_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test_Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('profession', models.CharField(max_length=100, verbose_name='מקצוע')),
                ('date', models.DateField(blank=True, default=datetime.date(2021, 1, 5), null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
            ],
            options={
                'verbose_name': 'Test_Schedule',
                'verbose_name_plural': 'Test_Schedule',
                'ordering': ['date'],
            },
        ),
        migrations.AlterField(
            model_name='board_class',
            name='publication_date',
            field=models.DateField(default=datetime.date(2021, 1, 5)),
        ),
        migrations.AlterField(
            model_name='board_school',
            name='publication_date',
            field=models.DateField(default=datetime.date(2021, 1, 5)),
        ),
    ]
