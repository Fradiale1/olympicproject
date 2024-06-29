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

    #atleti
    path('atleti', views.athlete, name='atleti'),
    path('update-athlete/', views.update_athlete, name='update_athlete'),
    path('delete-athlete/', views.delete_athlete, name='delete_athlete'),



    #path del template
    path('static_navigation', views.static_navigation, name='static_navigation'),
    path('light_sidenav', views.light_sidenav, name='light_sidenav'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('not_authenticated_request', views.not_authenticated_request, name='not_authenticated_request'),
    path('not_found', views.not_found, name='not_found'),
    path('internal_server_error', views.internal_server_error, name='internal_server_error'),
    path('charts', views.charts, name='charts'),
    path('tables', views.tables, name='tables'),
    

    #Path per la registrazione di tutte le View del Backend funzionante con request mapping. Si crea una classe view, si definiscono le request mapping in questa classe creata
    #e si registra la view creata in urlpattern
    path('', include(urlpattern)) 
]
