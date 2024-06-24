# olympicproject/urls.py

from django.urls import path, include
from . import views
from olympics.Views.AthleteView import AthleteView
from olympics.Views.HostView import HostView
from olympics.Views.MedalView import MedalView
from olympics.Views.ResultView import ResultView
from django_request_mapping import UrlPattern

urlpattern = UrlPattern()
#Registrazione delle view del backend
urlpattern.register(AthleteView)
urlpattern.register(HostView)
urlpattern.register(MedalView)
urlpattern.register(ResultView)

urlpatterns = [
    #path('', views.olympics),
    path('', views.index, name='index'),

    #Path per la registrazione di tutte le View del Backend funzionante con request mapping. Si crea una classe view, si definiscono le request mapping in questa classe creata
    #e si registra la view creata in urlpattern
    path('', include(urlpattern)) 
]
