# Generated by Django 3.2.4 on 2022-01-07 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplaced',
            name='couponapplied',
            field=models.CharField(default='None', max_length=150),
        ),
    ]
