from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Athlete
from olympics.Views.AthleteView import AthleteView
from olympics.Views.HostView import HostView
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def athlete(request):
    athlete_view = AthleteView()
    athletes_data = athlete_view.get_all_athletes(request).content  # Chiamata alla funzione get_all_athletes
    athletes = json.loads(athletes_data)  # Decodifica del JSON
    return render(request, 'features/athlete.html', {'athletes': athletes})

@csrf_exempt
def update_athlete(request):
    if request.method == 'POST':
        athlete_id = request.POST.get('athlete_id')
        athlete_view = AthleteView()

        url = reverse('atleti')
        response = HttpResponseRedirect(url)
        response.set_cookie('messaggio', 'Atleta aggiornato')
        response.set_cookie('codice_messaggio', '200')
        return response
    
    return HttpResponse(status=405)

@csrf_exempt
def delete_athlete(request):
    if request.method == 'POST':
        athlete_id = request.POST.get('athlete_id_delete')
        athlete_view = AthleteView()
        delete_athlete_message = athlete_view.delete_athlete(request, athlete_id).content

        # Esegui il reindirizzamento alla vista di destinazione
        #return redirect('atleti')
        url = reverse('atleti')
        response = HttpResponseRedirect(url)
        response.set_cookie('messaggio', 'Atleta Eliminato')
        response.set_cookie('codice_messaggio', '200')
        return response
    
    return HttpResponse(status=405)

 #def host(request):
 #   host_view = HostView()
 #   hosts_data = host_view.get_all_hosts(request).content  # Chiamata alla funzione get_all_athletes
 #   hosts = json.loads(hosts_data)  # Decodifica del JSON
 #   return render(request, 'features/athlete.html', {'hosts': hosts})
def host(request):
    host_view = HostView()
    host_data = host_view.get_all_hosts(request).content  # Chiamata alla funzione get_all_hosts
    hosts = json.loads(host_data)  # Decodifica del JSON
    return render(request, 'features/host.html', {'hosts': hosts})



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

