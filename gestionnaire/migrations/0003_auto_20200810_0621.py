# Generated by Django 3.0.7 on 2020-08-10 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionnaire', '0002_auto_20200712_1045'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Commentaire',
        ),
        migrations.RemoveField(
            model_name='moyennegenerale',
            name='eleve',
        ),
        migrations.RemoveField(
            model_name='moyennegenerale',
            name='enseignant_principal',
        ),
        migrations.RemoveField(
            model_name='note',
            name='eleve',
        ),
        migrations.RemoveField(
            model_name='note',
            name='enseignant',
        ),
        migrations.RemoveField(
            model_name='note',
            name='matiere',
        ),
        migrations.RemoveField(
            model_name='enseignant',
            name='utilisateur',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='utilisateur',
        ),
        migrations.DeleteModel(
            name='Moyenne',
        ),
        migrations.DeleteModel(
            name='MoyenneGenerale',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]
