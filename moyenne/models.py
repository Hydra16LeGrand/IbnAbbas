from django.db import models

import gestionnaire
# Create your models here.


class MoyenneGenerale(models.Model):

	moyenne_generale = models.FloatField()
	remarque = models.CharField(max_length=255, blank=True)
	commentaire = models.TextField(blank=True)
	decision = models.CharField(max_length=100)
	annee_scolaire = models.CharField(max_length=20)
	
	date = models.DateTimeField(auto_now_add = True)

	classe = models.OneToOneField(gestionnaire.models.Classe, on_delete=models.CASCADE, blank=True)


class Moyenne(models.Model):

	moyenne = models.FloatField()
	remarque = models.CharField(max_length=255, blank=True)
	commentaire = models.TextField(blank=True)
	date = models.DateTimeField(auto_now_add = True)
	periode = models.CharField(max_length=20)

	moyenne_generale = models.ForeignKey(MoyenneGenerale, on_delete=models.CASCADE)


class Note(models.Model):

	note = models.FloatField()
	remarque = models.CharField(max_length=255, blank=True)
	date = models.DateTimeField(auto_now_add = True)

	eleve = models.ForeignKey(gestionnaire.models.Eleve, on_delete=models.CASCADE)
	enseignant = models.ForeignKey(gestionnaire.models.Enseignant, on_delete=models.CASCADE)
	matiere = models.ForeignKey(gestionnaire.models.Matiere, on_delete=models.CASCADE)

	moyenne = models.ForeignKey(Moyenne, on_delete = models.CASCADE)