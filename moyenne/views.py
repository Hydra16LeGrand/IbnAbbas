from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse

from . import forms
import gestionnaire

import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyDboRB0gMywWU-5K7SmMn52XYlZqJvasl4",
    'authDomain': "ibnabbas-b0f83.firebaseapp.com",
    'databaseURL': "https://ibnabbas-b0f83.firebaseio.com",
    'projectId': "ibnabbas-b0f83",
    'storageBucket': "ibnabbas-b0f83.appspot.com",
    'messagingSenderId': "144639545086",
    'appId': "1:144639545086:web:04c08594f6cc80438b5faf",
    'measurementId': "G-HJ1QFDWXP6"
}

firebase = pyrebase.initialize_app(firebaseConfig)
authentification = firebase.auth()
database = firebase.database()


# Create your views here.

def login(request):

    if request.method == 'POST':

        form = forms.Login(request.POST)

        if form.is_valid():

            try:
                utilisateur = authentification.sign_in_with_email_and_password(form.cleaned_data['email'], form.cleaned_data['password'])
            except Exception as e:
                message = "CVotre session a expiree"
                return render(request, 'login.html', {'form': form, 'message': message})
            else:
                try:
                    infos = authentification.get_account_info(utilisateur['idToken'])
                except Exception as e:
                    return render(request, "login.html", {'message': "Impossible de reccuperer les informations sur cet utilisateur"})
                else:
                    emailVerified = infos['users'][0]['emailVerified']

                    if emailVerified:

                        request.session['uid'] = str(utilisateur['idToken'])
                        # uid = infos['users'][0]['localId']
                        return redirect('dashboard')
                    else:
                        return render(request, "login.html", {'form': forms.Login(),
                                                                      'message': "Veuillez confirmer d'abord votre compte en cliquant sur le lien recu par mail"})
        else:
            return render(request, "login.html", {'form': forms.Login(), 'message': "formulaire invalide"})

    else:
        return render(request, "login.html", {'form': forms.Login()})

def sign_up(request):

    def fonc_sign_up(infos_connexion, infos_sup):

        try:
            utilisateur = authentification.create_user_with_email_and_password(
                form.cleaned_data['email'], form.cleaned_data['password'])

        except:
            message = "Desole ! Un compte associe a cet email existe deja"
            return render(request, 'sign_up.html',
                          {'message': message, 'form': form})
        else:
            uid = utilisateur['localId']
            infos = authentification.get_account_info(utilisateur['idToken'])
            # print("infos : " + str(infos))
            # print("utilisateur : " + str(utilisateur))
            authentification.send_email_verification(utilisateur['idToken'])

            database.child(uid).child("infos_connexion").set(infos_connexion)
            database.child(uid).child("infos_supplementaire").set(infos_sup)

    print("yo")

    if request.method == 'POST':

        form = forms.Sign_up(request.POST)

        if form.is_valid():

            if form.cleaned_data['password'] == form.cleaned_data['c_password']:

                if len(form.cleaned_data['password']) >= 6:

                    existance = False   
                    if form.cleaned_data['qui'] == 'parent':

                        les_parents = gestionnaire.models.Parent.objects.all()

                        for parent in les_parents:

                            if form.cleaned_data['email'] == parent.email_parent:
                                existance = True

                                infos_connexion = {
                                    # 'username': form.cleaned_data['username'],
                                    'email': parent.email_parent,
                                    'password': form.cleaned_data['password']
                                }

                                infos_sup = {

                                    'qui': 'parent', # Parent ou enseignant
                                    'nom': parent.nom_parent,
                                    'prenom': parent.prenom_parent,
                                    'adresse': parent.adresse_parent,
                                    'telephone': parent.num_tel_parent,
                                    'id_enfant': parent.eleve_id,
                                    'lien': parent.lien_de_parente,
                                    'date_creation': str(parent.date_ajout),
                                    'date_modification': str(parent.date_modification)
                                }

                                fonc_sign_up(infos_connexion, infos_sup)
                    else:
                        
                        les_enseignants = gestionnaire.models.Enseignant.objects.all()

                        for enseignant in les_enseignants:

                            if form.cleaned_data['email'] == enseignant.email_enseignant:

                                existance = True

                                infos_connexion = {
                                    # 'username': form.cleaned_data['username'],
                                    'email': enseignant.email_enseignant,
                                    'password': form.cleaned_data['password']
                                }

                                infos_sup = {

                                    'qui': "enseignant", # Parent ou enseignant
                                    'nom': enseignant.nom_enseignant,
                                    'prenom': enseignant.prenom_enseignant,
                                    'adresse': enseignant.adresse_enseignant,
                                    'telephone': enseignant.num_tel_enseignant,
                                    'groupe_enseigne': str(enseignant.groupe),
                                    'salaire': enseignant.salaire,
                                    'ancienne_profession': enseignant.ancienne_profession,
                                    'date_creation': str(enseignant.date_ajout),
                                    'date_modification': str(enseignant.date_modification)
                                }

                                fonc_sign_up(infos_connexion, infos_sup)

                    if existance == True:

                        message = " Un mail contenant un lien vous a ete envoye. Veuillez cliquer sur le lien recu par mail pour confirmer votre compte!"
                        form = forms.Login()
                        return render(request, 'login.html', {'form': form, 'message': message})
                    else:
                        message = "Veuillez vous rendre a l'ecole afin de vous enregistrer."
                        return render(request, 'sign_up.html', {'message': message, 'form': form})

                else:
                    message = "Le mot de passe doit contenir au moins 6 caracteres"
                    return render(request, 'sign_up.html', {'message': message, 'form': form})

            else:
                message = 'Les mots de passe ne correspondent pas'
                return render(request, 'sign_up.html', {'message': message, 'form': form})

        else:

            message = 'Formulaire invalide'
            return render(request, 'sign_up.html', {'message': message, 'form': form})

    else:
        print("ya")
        form = forms.Sign_up()

        return render(request, 'sign_up.html', {'form': form})

def dashboard(request):

    try:
        mon_idToken = request.session['uid']
    except Exception as e:
        return redirect("login")
    else:
        try:
            infos = authentification.get_account_info(mon_idToken)
            uid = infos["users"][0]["localId"]
            infos_connexion = database.child(uid).child("infos_connexion").get()
            infos_sup = database.child(uid).child("infos_supplementaire").get()
        except Exception as e:
            message = "Les informations concernant cet utilisateur n'existe plus"
            return render(request, "login.html", {'message':message})
        else:
            if database.child(uid).child("infos_supplementaire").get().val()['qui'] == "parent":
                return render(request, "parent/dashboard.html", {
                    'infos_connexion':infos_connexion.val(),
                    'infos_sup':infos_sup.val()
                    })
            else:
                return render(request, "enseignant/dashboard.html", {
                    'infos_connexion':infos_connexion.val(),
                    'infos_sup':infos_sup.val()
                    })

def logout(request):

        auth.logout(request)
        return redirect('login')



def reccup_email(request):

    infos = authentification.get_account_info(request.session['uid'])
    uid = infos["users"][0]["localId"]
    email = database.child(uid).child('infos_connexion').get().val()['email']
    return email


def verif_enseignant_classe(request, id_classe):

    try:
         email = reccup_email(request)
    except Exception as e:
        raise e
    else:
        enseignant = gestionnaire.models.Enseignant.objects.get(email_enseignant = email)
        verif = False

        for classe in enseignant.classe.all():

            if classe.id == id_classe:
                verif = True

                return True

        return False

class Enseignant:


    def profils():

        pass

    def mes_classes(request):

        try:
            email = reccup_email(request)
        except Exception as e:
            raise e
        else:

            return render(request, 'enseignant/mes_classes.html', {'enseignant':gestionnaire.models.Enseignant.objects.get(email_enseignant=email)})

    def mes_eleves(request, id_classe):

        try:
            verif = verif_enseignant_classe(request, id_classe)
        except Exception as e:
            raise e
        else:
            if not verif:
                return redirect('mes_classes')
            else:
                try:
                    classe = gestionnaire.models.Classe.objects.get(id = id_classe)
                    email = reccup_email(request)
                    enseignant = gestionnaire.models.Enseignant.objects.get(email_enseignant=email)
                    
                except Exception as e:
                    raise e
                else:
                    matieres = []
                    for grp in enseignant.groupe.all():
                        for matiere in gestionnaire.models.Matiere.objects.filter(groupe=grp):
                            matieres.append(matiere)
                    # for eleve in classe.eleve.all():

                    #     print(eleve.nom_eleve)
                    return render(request, 'enseignant/mes_eleves.html',  {'classe':classe, 'matieres': matieres})

    def noter_les_eleves(request, id_classe):

        try:
            verif = verif_enseignant_classe(request, id_classe)
        except Exception as e:
            raise e
        else:
            pass
            # if not verif:

            #     return 
        return render(request, 'enseignant/mes_eleves.html')
       