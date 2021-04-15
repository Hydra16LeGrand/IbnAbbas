from django import forms


class Login(forms.Form):
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Mot de passe')


class Sign_up(forms.Form):

	email = forms.EmailField(label='E-mail')
	qui = forms.CharField(label='Parent ou enseignant')
	password = forms.CharField(label='Mot de passe')
	c_password = forms.CharField(label='Confirmer')
