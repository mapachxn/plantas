# Generated by Django 5.1.3 on 2024-11-26 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planta',
            name='imagenPlanta',
            field=models.ImageField(blank=True, null=True, upload_to='planta/'),
        ),
    ]
