# Generated by Django 5.1.3 on 2024-12-04 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_planta_imagenplanta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planta',
            name='imagenPlanta',
        ),
        migrations.RemoveField(
            model_name='planta',
            name='nombreCientifico',
        ),
        migrations.AddField(
            model_name='planta',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
        migrations.AlterField(
            model_name='planta',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='planta',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]