from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, logout, login

from . import models
from . import forms

# Create your views here.

# class DashboardViewParent(TemplateView):
# 	template_name = "account/dashboard_parent.html"

# class DashboardViewEnseignant(TemplateView):
# 	template_name = "account/dashboard_enseignant.html"

def accueil(request):
	return render(request, 'accueil.html')


class Parent:

	def lister_parent(request):

		return render(request,'parent/lister_parent.html', {'parents':models.Parent.objects.all(), 'eleves':models.Eleve.objects.all()})

	def enregistrer_parent(request, id_eleve):

		if request.method=='POST':

			form = forms.Parent(request.POST, request.FILES)
			
			# return HttpResponse(form_auth)
			if form.is_valid():


				nom_parent = form.cleaned_data['nom_parent']
				prenom_parent = form.cleaned_data['prenom_parent']
				adresse_parent = form.cleaned_data['adresse_parent']
				email_parent = form.cleaned_data['email_parent']
				lien_de_parente = form.cleaned_data['lien_de_parente']
				num_tel_parent = form.cleaned_data['num_tel_parent']
				nationalite_parent = form.cleaned_data['nationalite_parent']
				profession = form.cleaned_data['profession']
				image = form.cleaned_data['image']
				antecedant_judiciaire = form.cleaned_data['antecedant_judiciaire']
				situation_financiere = form.cleaned_data['situation_financiere']
				

				id_eleve = models.Eleve.objects.get(id=id_eleve)
				models.Parent.objects.create(
					nom_parent = nom_parent, 
					prenom_parent = prenom_parent, 
					adresse_parent = adresse_parent, 
					email_parent = email_parent,
					lien_de_parente = lien_de_parente,
					nationalite_parent = nationalite_parent,
					num_tel_parent = num_tel_parent,
					profession = profession,
					eleve = id_eleve,
					image=image,
					situation_financiere=situation_financiere,
					antecedant_judiciaire=antecedant_judiciaire
					
					)
				return HttpResponse("Parent enregistrer avec succes")

			else:
				return HttpResponse("Formulaire invalide")

		else:
			form = forms.Parent()
			return render(request, 'parent/enregistrer_parent.html', {'form':form, 'id_eleve':id_eleve})
			

	def supprimer_parent(request,id_parent):

		parent_a_supprimer = models.Parent.objects.get(id=id_parent)
		parent_a_supprimer.delete()

		return HttpResponse("Parent Supprimer avec succes")

	def modifier_parent(request,id_parent):

		parent_a_modifier = models.Parent.objects.get(id=id_parent)

		if request.method=='POST':
			form = forms.Parent(request.POST, request.FILES)

			# return HttpResponse(form)
			if form.is_valid():
				
				parent_a_modifier.nom_parent = form.cleaned_data['nom_parent']
				parent_a_modifier.prenom_parent = form.cleaned_data['prenom_parent']
				parent_a_modifier.adresse_parent = form.cleaned_data['adresse_parent']
				parent_a_modifier.email_parent = form.cleaned_data['email_parent']
				parent_a_modifier.lien_de_parente = form.cleaned_data['lien_de_parente']
				parent_a_modifier.num_tel_parent = form.cleaned_data['num_tel_parent']
				parent_a_modifier.nationalite_parent = form.cleaned_data['nationalite_parent']
				parent_a_modifier.profession = form.cleaned_data['profession']

				parent_a_modifier.image = form.cleaned_data['image']
				parent_a_modifier.antecedant_judiciaire = form.cleaned_data['antecedant_judiciaire']
				parent_a_modifier.situation_financiere = form.cleaned_data['situation_financiere']

				parent_a_modifier.save()

				return HttpResponse("Parent modifier avec succes")

			else:
				return HttpResponse("Formulaire invalide")

		else:

			form = forms.Parent()
			return render(request, 'parent/modifier_parent.html', {'form':form,'parent_a_modifier':parent_a_modifier})

class Eleve:

	def lister_eleve(request):

		return render(request, 'eleve/lister_eleve.html', {'eleves':models.Eleve.objects.all()})

	def supprimer_eleve(request, id_eleve):

		eleve_a_supprimer = models.Eleve.objects.get(id=id_eleve)

		eleve_a_supprimer.delete()

		return HttpResponse("Eleve Supprimer avec succes")

	def modifier_eleve(request, id_eleve):

		eleve_a_modifier = models.Eleve.objects.get(id=id_eleve)

		if request.method == 'POST':

			form = forms.Eleve(request.POST, request.FILES)
			if form.is_valid():
				
				eleve_a_modifier.nom_eleve = form.cleaned_data['nom_eleve']
				eleve_a_modifier.prenom_eleve = form.cleaned_data['prenom_eleve']
				eleve_a_modifier.date_naissance_eleve = form.cleaned_data['date_naissance_eleve']
				eleve_a_modifier.adresse_eleve = form.cleaned_data['adresse_eleve']
				eleve_a_modifier.num_tel_eleve = form.cleaned_data['num_tel_eleve']
				eleve_a_modifier.nationalite_eleve = form.cleaned_data['nationalite_eleve']
				eleve_a_modifier.image = form.cleaned_data['image']
				eleve_a_modifier.status_scolarite = form.cleaned_data['status_scolarite']
				eleve_a_modifier.reste_a_payer = form.cleaned_data['reste_a_payer']

				eleve_a_modifier.save()

				return HttpResponse("Eleve modifier avec succes")

			else:
				return HttpResponse("Formulaire invalide")

		else:
			form = forms.Eleve()

			return render(request, 'eleve/modifier_eleve.html', {'form':form, 'eleve_a_modifier':eleve_a_modifier})

	def enregistrer_eleve(request):

		if request.method == 'POST':
			form = forms.Eleve(request.POST, request.FILES)
			# form2 = forms.Eleve(request.FILES)
			# return HttpResponse(form)
			if form.is_valid():
				choix_classes = form.cleaned_data['classe']

				nom_eleve = form.cleaned_data['nom_eleve']
				prenom_eleve = form.cleaned_data['prenom_eleve']
				adresse_eleve = form.cleaned_data['adresse_eleve']
				date_naissance_eleve = form.cleaned_data['date_naissance_eleve']
				num_tel_eleve = form.cleaned_data['num_tel_eleve']
				nationalite_eleve = form.cleaned_data['nationalite_eleve']

				status_scolarite = form.cleaned_data['status_scolarite']
				reste_a_payer = form.cleaned_data['reste_a_payer']
				image = form.cleaned_data['image']
				# Enregistrement d'un eleve
				eleve_a_enregistrer = models.Eleve(
					nom_eleve = nom_eleve, 
					prenom_eleve = prenom_eleve, 
					adresse_eleve = adresse_eleve, 
					date_naissance_eleve = date_naissance_eleve, 
					nationalite_eleve = nationalite_eleve,
					num_tel_eleve = num_tel_eleve,

					matricule = "TEMP",
					status_scolarite = status_scolarite,
					reste_a_payer = reste_a_payer,
					image = image
					)
				eleve_a_enregistrer.save()
				for classe in choix_classes:
					eleve_a_enregistrer.classe.add(classe)

				return HttpResponse("Eleve enregistrer avec succes")

			else:
				return HttpResponse("Formulaire invalide")
		else:
			form = forms.Eleve()
			return render(request, 'eleve/enregistrer_eleve.html',{'form':form})

class Enseignant:

	def lister_enseignant(request):

		# liste=[]
		# for enseignant in models.Enseignant.objects.all():

		# 	for ens in enseignant.groupe.all():
		# 		liste.append(ens.id)
		# 	# 	for groupe_t in models.Groupe.objects.all():
		# 	# 		if groupe_t.id == ens:
		# 	# 			liste.append(groupe_t.groupe)
		# return HttpResponse(liste)
		return render(request,'enseignant/lister_enseignant.html', {'enseignants':models.Enseignant.objects.all(), 'groupes':models.Groupe.objects.all()})

	def enregistrer_enseignant(request):

		if request.method == 'POST':

			form = forms.Enseignant(request.POST, request.FILES)
			# return HttpResponse(form)
			if form.is_valid() :

				# les_utilisateurs = models.User.objects.all()

				# verif = False
				# for util in les_utilisateurs:
				# 	if util.username == form_auth.cleaned_data['login']:
				# 		verif = True

				nom_enseignant = form.cleaned_data['nom_enseignant']
				prenom_enseignant = form.cleaned_data['prenom_enseignant']
				date_naissance = form.cleaned_data['date_naissance_enseignant']
				adresse_enseignant = form.cleaned_data['adresse_enseignant']
				e_mail = form.cleaned_data['email_enseignant']
				num_tel_enseignant = form.cleaned_data['num_tel_enseignant']
				nationalite = form.cleaned_data['nationalite']
				autre_profession = form.cleaned_data['autre_profession']
				prof_de = form.cleaned_data['prof_de']

				regularite = form.cleaned_data['regularite']
				antecedant_judiciaire = form.cleaned_data['antecedant_judiciaire']
				image = form.cleaned_data['image']
				ancienne_profession = form.cleaned_data['ancienne_profession']
				salaire = form.cleaned_data['salaire']
				periode = form.cleaned_data['periode']

				# return HttpResponse()
				enseignant_a_enregistrer = models.Enseignant(
					nom_enseignant = nom_enseignant,
					prenom_enseignant = prenom_enseignant, 
					date_naissance_enseignant = date_naissance, 
					adresse_enseignant = adresse_enseignant, 
					email_enseignant = e_mail, 
					num_tel_enseignant = num_tel_enseignant, 
					nationalite_enseignant = nationalite, 
					autre_profession = autre_profession,

					regularite = regularite,
					antecedant_judiciaire = antecedant_judiciaire,
					image = image,
					ancienne_profession = ancienne_profession,
					salaire = salaire,
					periode = periode,
					)
				enseignant_a_enregistrer.save()

				for prof_de_temp in prof_de:
					enseignant_a_enregistrer.groupe.add(prof_de_temp)

				return HttpResponse("Enseignant enregistrer avec succes")

			else:
				return HttpResponse("Formulaire invalide")

		else:
			form = forms.Enseignant()

			return render(request, 'enseignant/enregistrer_enseignant.html', {'form':form})

	def supprimer_enseignant(request, id_enseignant):

		enseignant_a_supprimer = models.Enseignant.objects.get(id=id_enseignant)

		enseignant_a_supprimer.delete()

		return HttpResponse("Enseignant supprimer avec succes")

	def modifier_enseignant(request, id_enseignant):

		enseignant_a_modifier = models.Enseignant.objects.get(id=id_enseignant)

		if request.method == 'POST':
			form = forms.Enseignant(request.POST, request.FILES)
			if form.is_valid():

				enseignant_a_modifier.nom_enseignant = form.cleaned_data['nom_enseignant']
				enseignant_a_modifier.prenom_enseignant = form.cleaned_data['prenom_enseignant']
				enseignant_a_modifier.date_naissance_enseignant = form.cleaned_data['date_naissance_enseignant']
				enseignant_a_modifier.adresse_enseignant = form.cleaned_data['adresse_enseignant']
				enseignant_a_modifier.email_enseignant = form.cleaned_data['email_enseignant']
				enseignant_a_modifier.autre_profession = form.cleaned_data['autre_profession']
				enseignant_a_modifier.nationalite_enseignant = form.cleaned_data['nationalite']
				enseignant_a_modifier.num_tel_enseignant = form.cleaned_data['num_tel_enseignant']

				enseignant_a_modifier.regularite = form.cleaned_data['regularite']
				enseignant_a_modifier.antecedant_judiciaire = form.cleaned_data['antecedant_judiciaire']
				enseignant_a_modifier.image = form.cleaned_data['image']
				enseignant_a_modifier.ancienne_profession = form.cleaned_data['ancienne_profession']
				enseignant_a_modifier.salaire = form.cleaned_data['salaire']
				enseignant_a_modifier.periode = form.cleaned_data['periode']

				enseignant_a_modifier.save()

				for prof_de_temp in form.cleaned_data['prof_de']:
					enseignant_a_modifier.groupe.add(int(prof_de_temp))

				return HttpResponse("Enseignant modifier avec succes")

			else:
				return HttpResponse("Formulaire invalide")

		else:
			form = forms.Enseignant()

			return render(request, 'enseignant/modifier_enseignant.html', {'form':form, 'enseignant_a_modifier':enseignant_a_modifier})


# class Authentification:

# 	def auth_enseignant(request):

# 		if request.method == 'POST':

# 			form = forms.Authentification(request.POST)

# 			if form.is_valid():
				
# 				login = form.cleaned_data['login']
# 				password = form.cleaned_data['mdp']
# 				user_enseignant = authenticate(username=login, password=password)

# 				if user_enseignant is not None:

					# login(request, user_enseignant)
# 					return render(request, 'account/dashboard_enseignant.html', {'user_enseignant':user_enseignant})

# 				else:

# 					msg = "Utilisateur inexistant"
# 					return render(request, 'account/login_enseignant.html', {'msg':msg})
# 			else:
# 				msg = "Formulaire invalide"
# 				return render(request, 'account/login_enseignant.html', {'msg':msg})

# 		else:

# 			form = forms.Authentification()

# 			return render(request, 'account/login_enseignant.html', {'form': form})


# 	def logout_enseignant(request):

# 		logout(request)

# 		form = forms.Authentification()

# 		return render(request, 'account/login_enseignant.html', {'form': form})