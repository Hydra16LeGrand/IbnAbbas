# Generated by Django 3.0.7 on 2020-09-06 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionnaire', '0004_matiere_coefficient'),
    ]

    operations = [
        migrations.AddField(
            model_name='enseignant',
            name='classe',
            field=models.ManyToManyField(related_name='enseignant', to='gestionnaire.Classe'),
        ),
    ]
