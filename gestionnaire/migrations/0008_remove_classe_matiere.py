# Generated by Django 3.0.7 on 2020-11-12 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionnaire', '0007_auto_20201112_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classe',
            name='matiere',
        ),
    ]