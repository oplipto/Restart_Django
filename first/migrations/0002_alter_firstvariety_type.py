# Generated by Django 5.0.6 on 2024-05-25 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstvariety',
            name='type',
            field=models.CharField(choices=[('LG', 'Lamborghini Gallardo'), ('FR', 'Ferrari'), ('BM', 'BMW'), ('AU', 'Audi'), ('MB', 'Mercedes Benz')], default='LG', max_length=2),
        ),
    ]
