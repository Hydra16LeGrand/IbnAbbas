from django import forms


class Eleve(forms.Form):

	choix_classes=[

		('1',"1ere Annee Arabe"),
		('2',"1ere Annee Coran"),
		('3',"1ere Annee Francais"),
		('4',"2eme Annee Arabe"),
		('5',"2eme Annee Coran"),
		('6',"2eme Annee Francais"),
		('7',"3eme Annee Arabe"),
		('8',"3eme Annee Coran"),
		('9',"3eme Annee Francais"),
		('10',"4eme Annee Arabe"),
		('11',"4eme Annee Coran"),
		('12',"4eme Annee Francais"),
		('13',"5eme Annee Arabe"),
		('14',"5eme Annee Coran"),
		('15',"5eme Annee Francais"),
		('16',"6eme Annee Arabe"),
		('17',"6eme Annee Coran"),
		('18',"6eme Annee Francais"),

	]
	nom_eleve = forms.CharField(label="Nom de l'eleve", max_length=100)
	prenom_eleve = forms.CharField(label="Prenom de l'eleve", max_length=100)
	date_naissance_eleve = forms.DateField(label="Date de naissance")
	adresse_eleve = forms.CharField(label="Adresse du parent", max_length=100)
	num_tel_eleve = forms.CharField(label="Numero de telephone", max_length=100)
	nationalite_eleve = forms.CharField(label='Nationalite eleve', max_length=100)
	classe = forms.MultipleChoiceField(
		label='choix de classe',
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=choix_classes,
    )

	image = forms.ImageField()
	status = [
		(True, 'Solder'),
		(False, 'Non Solder')
	]
	status_scolarite = forms.ChoiceField(label="Status de la scolarite", widget=forms.Select(), choices=status, required=True, initial='')
	reste_a_payer = forms.IntegerField(label="Reste de la scolarite a payer")

class Parent(forms.Form):

	prenom_parent = forms.CharField(label='Prenom du parent', max_length=100)
	nom_parent = forms.CharField(label='Nom du parent', max_length=100)
	adresse_parent = forms.CharField(label='Adresse du parent', max_length=100)
	lien_de_parente = forms.CharField(label="Lien de parente", max_length = 100)
	num_tel_parent = forms.CharField(label="Numero de telephone", max_length=100)
	nationalite_parent = forms.CharField(label='Nationalite parent', max_length=100)
	profession = forms.CharField(label="Profession", max_length=100)
	email_parent = forms.EmailField(label="E-mail du parent")

	
	antecedant_judiciaire = forms.CharField(widget =forms.Textarea, label="Les infos sur le casier judiciaire du parent")
	image=forms.ImageField(label="Photo du parent")
	sit_fin=[
		(True, 'Stable'),
		(False, 'Instable')
	]
	situation_financiere = forms.ChoiceField(label="Situation financiaire du parent", widget=forms.Select(), choices=sit_fin, required=True)

class Enseignant(forms.Form):

	prof_de_temp=[
		('1', 'Arabe'),
		('2', 'Coran'),
		('3', 'Francais')
	]
	nom_enseignant = forms.CharField(label="Nom de l'enseignant", max_length=100)
	prenom_enseignant = forms.CharField(label="Prenom de l'enseignant", max_length=100)
	date_naissance_enseignant = forms.DateField(label="Date de naissance")
	adresse_enseignant = forms.CharField(label='Adresse du parent', max_length=100)
	email_enseignant = forms.EmailField(label = "E-mail")
	autre_profession = forms.CharField(label="Autre profession", max_length=100)
	nationalite = forms.CharField(label='Nationalite enseignant', max_length=100)
	num_tel_enseignant = forms.CharField(label="Numero de telephone", max_length=100)
	prof_de = forms.MultipleChoiceField(label="Prod de", widget=forms.CheckboxSelectMultiple, choices=prof_de_temp)

	antecedant_judiciaire = forms.CharField(widget = forms.Textarea, label="Les infos sur le casier judiciaire de l'enseignant")
	image=forms.ImageField(label="Photo de l'enseignant")
	ancienne_profession = forms.CharField(widget=forms.Textarea, label="Ancienne profession")
	salaire = forms.IntegerField(label="Salaire de l'enseignant")
	periode = forms.CharField(label="la periode de paiement de salaire")

	reg = [
		(1,'Enseignant permanent'),
		(0,'Enseignant non permanent')
	]
	regularite = forms.ChoiceField(label="enseignant permanent ou non", choices=reg, widget = forms.Select(), required=True)


# class Authentification(forms.Form):

# 	login = forms.CharField(label="Login de connexion du parent", max_length=100)
# 	mdp = forms.CharField(label="Mot de passe de connexion")
# 	c_mdp = forms.CharField(label="Confirmation du mot de passe")