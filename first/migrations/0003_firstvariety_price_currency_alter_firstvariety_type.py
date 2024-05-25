# Generated by Django 5.0.6 on 2024-05-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_alter_firstvariety_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstvariety',
            name='price_currency',
            field=models.CharField(default='USD', max_length=1000),
        ),
        migrations.AlterField(
            model_name='firstvariety',
            name='type',
            field=models.CharField(choices=[('LG', 'Lamborghini'), ('FR', 'Ferrari'), ('BM', 'BMW'), ('AU', 'Audi'), ('MB', 'Mercedes Benz')], default='LG', max_length=2),
        ),
    ]
