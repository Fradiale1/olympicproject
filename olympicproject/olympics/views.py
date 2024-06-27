from django.shortcuts import render
from olympics.Views.AthleteView import AthleteView
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def athlete(request):
    athlete_view = AthleteView()
    athletes_data = athlete_view.get_all_athletes(request).content  # Chiamata alla funzione get_all_athletes
    athletes = json.loads(athletes_data)  # Decodifica del JSON
    return render(request, 'features/athlete.html', {'athletes': athletes})

#view per le pagine del template
def static_navigation(request):
    return render(request, 'utils/layout-static.html')

def light_sidenav(request):
    return render(request, 'utils/layout-sidenav-light.html')

def login(request):
    return render(request, 'auth/login.html')

def register(request):
    return render(request, 'auth/register.html')

def forgot_password(request):
    return render(request, 'auth/password.html')

def not_authenticated_request(request):
    return render(request, 'errorPages/401.html')

def not_found(request):
    return render(request, 'errorPages/404.html')

def internal_server_error(request):
    return render(request, 'errorPages/500.html')

def charts(request):
    return render(request, 'utils/charts.html')

def tables(request):
    return render(request, 'utils/tables.html')

