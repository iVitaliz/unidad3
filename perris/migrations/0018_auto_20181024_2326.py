# Generated by Django 2.1.2 on 2018-10-25 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perris', '0017_auto_20181024_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perros_rescatados',
            name='estado',
            field=models.CharField(choices=[('Rescatado', 'Rescatado'), ('Disponible', 'Disponible'), ('Adoptado', 'Adoptado')], default='', max_length=10),
        ),
    ]
