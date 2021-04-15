# Generated by Django 3.0.7 on 2020-07-12 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestionnaire', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enseignant',
            name='login',
        ),
        migrations.RemoveField(
            model_name='enseignant',
            name='mdp',
        ),
        migrations.AddField(
            model_name='enseignant',
            name='utilisateur',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
