# Generated by Django 5.0.6 on 2024-05-26 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_firstvariety_price_currency_alter_firstvariety_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstvariety',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
