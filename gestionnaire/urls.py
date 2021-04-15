"""IbnAbbas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.conf.urls import url
# from django.contrib.auth.views import LoginView, LogoutView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # url(r'^login_parent/$', view=LoginView.as_view(template_name='account/login_parent.html', redirect_authenticated_user=True), name='login_parent'),
    # url(r'^login_enseignant/$', view=LoginView.as_view(template_name='account/login_enseignant.html'), name='login_enseignant'),

    # url(r'^logout_parent/$', LogoutView.as_view(), name='logout_parent'),

    # url(r'^login_parent/$', view=LoginView.as_view(template_name='account/login_parent.html', redirect_authenticated_user=True), name='login_parent'),
    # url(r'^login_enseignant/', view=views.Authentification.auth_enseignant, name='login_enseignant'),
    # url(r'^logout_enseignant/$', views.Authentification.logout_enseignant, name='logout_enseignant'),

    # url(r'^dashboard_parent/$',
    # view=views.DashboardViewParent.as_view(),
    # name='dashboard_parent'), url(r'^dashboard_enseignant/$',
    # view=views.DashboardViewEnseignant.as_view(),
    # name='dashboard_enseignant'),

    url(r'^$', views.accueil, name='accueil'),

    # urls en rapport avec Eleve
    url(r'^lister_eleve$', views.Eleve.lister_eleve, name="lister_eleve"),
    url(r'^modifier_eleve/(?P<id_eleve>\d+)', views.Eleve.modifier_eleve, name="modifier_eleve"),
    url(r'^supprimer_eleve/(?P<id_eleve>\d+)', views.Eleve.supprimer_eleve, name="supprimer_eleve"),
    url(r'^enregistrer_eleve/', views.Eleve.enregistrer_eleve, name="enregistrer_eleve"),

    # urls en rapport avec Enseignant
    url(r'^enregistrer_enseignant/', views.Enseignant.enregistrer_enseignant, name="enregistrer_enseignant"),
    url(r'^lister_enseignant$', views.Enseignant.lister_enseignant, name="lister_enseignant"),
    url(r'^modifier_enseignant/(?P<id_enseignant>\d+)', views.Enseignant.modifier_enseignant, name="modifier_enseignant"),
    url(r'^supprimer_enseignant/(?P<id_enseignant>\d+)', views.Enseignant.supprimer_enseignant, name="supprimer_enseignant"),

    # urls en rapport avec Parent
    url(r'lister_parent/', views.Parent.lister_parent, name='lister_parent'),
    url(r'enregistrer_parent/(?P<id_eleve>\d+)', views.Parent.enregistrer_parent, name='enregistrer_parent'),
    url(r'supprimer_parent/(?P<id_parent>\d+)', views.Parent.supprimer_parent, name='supprimer_parent'),
    url(r'modifier_parent/(?P<id_parent>\d+)', views.Parent.modifier_parent, name='modifier_parent'),

    # Autres urls 


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
