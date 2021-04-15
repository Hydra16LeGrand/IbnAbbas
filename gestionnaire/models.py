from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Niveau(models.Model):

	niveau = models.IntegerField()

	def __str__(self):

		return "Niveau ",self.niveau


class Groupe(models.Model):

	groupe = models.CharField(max_length = 8)
	

class Matiere(models.Model):

	matiere = models.CharField(max_length = 50)
	coefficient = models.IntegerField(blank=True)

	groupe = models.ForeignKey(Groupe, on_delete = models.CASCADE)


# Hypothese : Lorsqu'une classe apprend un groupe de matiere alors cette classe fait toutes les matiere de ce groupe
class Classe(models.Model):

	niveau = models.ForeignKey(Niveau, on_delete = models.CASCADE)
	groupe = models.ForeignKey(Groupe, on_delete = models.CASCADE)
	classe = models.CharField(max_length=100)
	description = models.CharField(max_length=100)

	matiere = models.ManyToManyField(Matiere, related_name='classe')
	

class Eleve(models.Model):

	nom_eleve = models.CharField(max_length=100)
	prenom_eleve = models.CharField(max_length=100)
	num_tel_eleve = models.CharField(max_length=100, blank=True)
	adresse_eleve = models.CharField(max_length=255)
	date_naissance_eleve = models.DateField(blank=True)
	nationalite_eleve = models.CharField(max_length=100)

	date_ajout = models.DateTimeField(auto_now_add = True)
	date_modification = models.DateTimeField(auto_now =True)

	classe = models.ManyToManyField(Classe, related_name='eleve')
	# matiere = models.ManyToManyField(Matiere, related_name='eleve')

	image = models.ImageField(upload_to="profils_eleves/", blank=True)
	matricule = models.CharField(max_length=100, blank=True)
	status_scolarite = models.BooleanField(blank=True)
	reste_a_payer = models.IntegerField(blank=True, default=0)


class Parent(models.Model):


	nom_parent = models.CharField(max_length = 100)
	prenom_parent = models.CharField(max_length = 100)
	adresse_parent = models.CharField(max_length = 255)
	num_tel_parent = models.CharField(max_length=100, blank = True)
	email_parent = models.EmailField(blank = True)
	profession = models.CharField(max_length=100)
	nationalite_parent = models.CharField(max_length=100)

	lien_de_parente = models.CharField(max_length = 100)

	date_ajout = models.DateTimeField(auto_now_add = True)
	date_modification = models.DateTimeField(auto_now=True)

	eleve = models.ForeignKey(Eleve, on_delete = models.CASCADE)

	# utilisateur = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
	antecedant_judiciaire = models.TextField(blank=True)
	image = models.ImageField(upload_to="profils_parents/", blank=True)
	situation_financiere = models.CharField(max_length=100, blank=True)
	

class Enseignant(models.Model):
	
	nom_enseignant = models.CharField(max_length = 100)
	prenom_enseignant = models.CharField(max_length = 100)
	adresse_enseignant = models.CharField(max_length = 255)
	num_tel_enseignant = models.CharField(max_length=100, blank = True)
	date_naissance_enseignant = models.DateField(blank = True)
	email_enseignant = models.EmailField(blank = True)
	autre_profession = models.CharField(max_length=100, blank=True)
	nationalite_enseignant = models.CharField(max_length=100)

	date_ajout = models.DateTimeField(auto_now_add = True)
	date_modification = models.DateTimeField(auto_now=True)

	groupe = models.ManyToManyField(Groupe, related_name = 'enseignant')
	classe = models.ManyToManyField(Classe, related_name = 'enseignant')
	# matiere = models.ManyToManyField(Matiere, related_name='enseignant')

	image = models.ImageField(upload_to="profils_enseignants/", blank=True)
	antecedant_judiciaire = models.TextField(blank=True)
	ancienne_profession = models.CharField(max_length=100, blank=True)
	salaire = models.IntegerField(blank=True)
	periode = models.CharField(max_length=100, blank=True)
	regularite = models.BooleanField(blank=True)

	# utilisateur = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)