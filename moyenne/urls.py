from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^login$', view=views.login, name='login'),
    url(r'^sign_up$', view=views.sign_up, name='sign_up'),
    url(r'^logout$', view=views.logout, name='logout'),
    url(r'^dashboard$|^$', view=views.dashboard, name='dashboard'),

    #Les methodes de la classe enseignant
    path('enseignant/mes_eleves/<int:id_classe>', view=views.Enseignant.mes_eleves, name='mes_eleves'),
    url(r'^enseignant/mes_classes/', view=views.Enseignant.mes_classes, name='mes_classes'),
    # path('enseignant/noter_un_eleve/<id_eleve>', view = views.Enseignant.noter_un_eleve, name='noter_un_eleve'),
    path('enseignant/noter_les_eleves/<int:id_classe>', view = views.Enseignant.noter_les_eleves, name='noter_les_eleves'),

]
