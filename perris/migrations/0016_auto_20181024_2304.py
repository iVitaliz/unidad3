# Generated by Django 2.1.2 on 2018-10-25 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perris', '0015_auto_20181024_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perros_rescatados',
            name='estado',
            field=models.CharField(choices=[('Rescatadi', 'Rescatado'), ('Disponible', 'Disponible'), ('Adoptado', 'Adoptado')], default='', max_length=1),
        ),
    ]
