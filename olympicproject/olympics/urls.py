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
    path('search_athlete', views.search_athlete, name='search_athlete'),
    path('create_athlete/', views.create_athlete, name='create_athlete'),
    path('update_athlete/', views.update_athlete, name='update_athlete'),
    path('delete_athlete/', views.delete_athlete, name='delete_athlete'),
    
    #host
    path('host', views.host, name='host'),
    path('search_host', views.search_host, name='search_host'),
    path('create_host/', views.create_host, name='create_host'),
    path('update_host/', views.update_host, name='update_host'),
    path('delete_host/', views.delete_host, name='delete_host'),
    

    #medaglie
    path('medaglie', views.medal, name='medaglie'),
    path('search_medal', views.search_medal, name='search_medal'),
    path('create_medal/', views.create_medal, name='create_medal'),
    path('update_medal/', views.update_medal, name='update_medal'),
    path('delete_medal/', views.delete_medal, name='delete_medal'),

    #risultati
    path('risultati', views.result, name='risultati'),
    path('search_result', views.search_result, name='search_result'),
    path('create_result/', views.create_result, name='create_result'),
    path('update_result/', views.update_result, name='update_result'),
    path('delete_result/', views.delete_result, name='delete_result'),




    #classifica
    path('placing', views.placing, name='placing'),
    path('fill_event', views.fill_event, name='fill_event'),
    path('search_placing', views.search_placing, name='search_placing'),

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
