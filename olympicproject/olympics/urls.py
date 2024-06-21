# olympicproject/urls.py

from django.urls import path, include
from . import views
from .views.AthleteView import AthleteView
from .views.HostView import HostView
from .views.MedalView import MedalView
from .views.ResultView import ResultView
from django_request_mapping import UrlPattern

urlpattern = UrlPattern()
#Registrazione delle view del backend
urlpattern.register(AthleteView)
urlpattern.register(HostView)
urlpattern.register(MedalView)
urlpattern.register(ResultView)

urlpatterns = [
    #path('', views.olympics),
    

    path('', include(urlpattern)) 
]
