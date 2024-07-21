from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from olympics.Views.AthleteView import AthleteView
from olympics.Views.HostView import HostView
from olympics.Views.MedalView import MedalView
from olympics.Views.ResultView import ResultView
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.paginator import Paginator
import json

# Creazione view Index
def index(request):
    return render(request, 'index.html')

# Creazione view Athele
def athlete(request):
    athletes = json.loads(AthleteView().get_all_athletes(request).content)  # Decodifica del JSON
    hosts = json.loads(HostView().get_all_hosts(request).content)

    paginator = Paginator(athletes, 12)  # 10 atleti per pagina

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'features/athlete.html', {'page_obj': page_obj, 'hosts': hosts}) #'athletes': athletes,


def search_athlete(request):
    string_searchbar = request.GET.get('string_searchbar')
    athletes = json.loads(AthleteView().search_athletes(request, string_searchbar).content)  # Decodifica del JSON
    hosts = json.loads(HostView().get_all_hosts(request).content)

    paginator = Paginator(athletes, 12)  # 10 atleti per pagina

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
   
    
    return render(request, 'features/athlete.html', {'page_obj': page_obj, 'hosts': hosts}) #'athletes': athletes,
    
@csrf_exempt
def create_athlete(request): 
    if request.method == 'POST':
        data = {
            'athlete_url': request.POST.get('athlete_url_create',''),
            'athlete_full_name': request.POST.get('athlete_full_name_create',''),
            'games_participations': request.POST.get('games_participations_create',''),
            'first_game': request.POST.get('first_game_create',''),
            'athlete_year_birth': request.POST.get('athlete_year_birth_create',''),
            'athlete_medals': request.POST.get('athlete_medals_create',''),
            'bio': request.POST.get('bio_create',''),
        }
        athlete_view = AthleteView()
        athlete_view.create_athlete(data).content

        url = reverse('atleti')
        response = HttpResponseRedirect(url)
        response.set_cookie('messaggio', 'Atleta Creato')
        response.set_cookie('codice_messaggio', '200')
        return response
    
    return HttpResponse(status=405)

@csrf_exempt
def update_athlete(request): 
    if request.method == 'POST':
        data = {
            '_id': request.POST.get('athlete_id_update',''),
            'athlete_url': request.POST.get('athlete_url_update',''),
            'athlete_full_name': request.POST.get('athlete_full_name_update',''),
            'games_participations': request.POST.get('games_participations_update',''),
            'first_game': request.POST.get('first_game_update',''),
            'athlete_year_birth': request.POST.get('athlete_year_birth_update',''),
            'athlete_medals': request.POST.get('athlete_medals_update',''),
            'bio': request.POST.get('bio_update',''),
        }

        athlete_view = AthleteView()
        athlete_view.update_athlete(data).content
     
        url = reverse('atleti')
        response = HttpResponseRedirect(url)
        response.set_cookie('messaggio', 'Atleta Aggiornato')
        response.set_cookie('codice_messaggio', '200')
        return response
    
    return HttpResponse(status=405)

@csrf_exempt
def delete_athlete(request):
    if request.method == 'POST':
        athlete_id = request.POST.get('athlete_id_delete')
        athlete_view = AthleteView()
        #delete_athlete_message = 
        athlete_view.delete_athlete(request, athlete_id).content

        # Esegui il reindirizzamento alla vista di destinazione
        #return redirect('atleti')
        url = reverse('atleti')
        response = HttpResponseRedirect(url)
        response.set_cookie('messaggio', 'Atleta Eliminato')
        response.set_cookie('codice_messaggio', '200')
        return response
    
    return HttpResponse(status=405)


# Creazione view Host
def host(request):
    hosts = json.loads(HostView().get_all_hosts(request).content)
    
    paginator = Paginator(hosts, 12)  # 10 host per pagina

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'features/host.html', {'page_obj': page_obj}) #'hosts': hosts,


def search_host(request):
    string_searchbar = request.GET.get('string_searchbar')
    season = request.GET.get('season')
    
    hosts = json.loads(HostView().search_hosts(request, string_searchbar, season).content)

    paginator = Paginator(hosts, 12)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
   
    
    return render(request, 'features/host.html', {'page_obj': page_obj}) #'athletes': athletes,

@csrf_exempt
def create_host(request): 
    if request.method == 'POST':
        data = {
           # 'game_slug': request.POST.get('slug_create',''),
            'game_end_date': request.POST.get('end_date_create',''),
            'game_start_date': request.POST.get('begin_date_create',''),
            'game_location': request.POST.get('location_create',''),
            'game_name': request.POST.get('game_name_create',''),
            'game_season': request.POST.get('season_create',''),
            'game_year': request.POST.get('game_year_create',''),
        }
        host_view = HostView()
        host_view.create_host(data).content

        url = reverse('host')
        response = HttpResponseRedirect(url)
        response.set_cookie('messaggio', 'host aggiornato')
        response.set_cookie('codice_messaggio', '200')
        return response
    
    return HttpResponse(status=405)

@csrf_exempt
def update_host(request):  
    if request.method == 'POST':
        data = {
            '_id': request.POST.get('host_id_update',''),
          #  'game_slug': request.POST.get('slug_update',''),
            'game_end_date': request.POST.get('end_date_update',''),
            'game_start_date': request.POST.get('begin_date_update',''),
            'game_location': request.POST.get('location_update',''),
            'game_name': request.POST.get('game_name_update',''),
            'game_season': request.POST.get('season_update',''),
            'game_year': request.POST.get('game_year_update',''),
        }

        host_view = HostView()
        host_view.update_host(data).content
     
        url = reverse('host')
        response = HttpResponseRedirect(url)
        response.set_cookie('messaggio', 'Host aggiornato')
        response.set_cookie('codice_messaggio', '200')
        return response
    
    return HttpResponse(status=405)

@csrf_exempt
def delete_host(request):
    if request.method == 'POST':
        host_id = request.POST.get('host_id_delete')
        host_view = HostView()
        #delete_athlete_message = 
        host_view.delete_host(request, host_id).content

        # Esegui il reindirizzamento alla vista di destinazione
        #return redirect('atleti')
        url = reverse('host')
        response = HttpResponseRedirect(url)
        response.set_cookie('messaggio', 'Host Eliminato')
        response.set_cookie('codice_messaggio', '200')
        return response
    
    return HttpResponse(status=405)

def medal(request):

    athletes = json.loads(AthleteView().get_all_athletes(request).content)  # Decodifica del JSON
    medals = json.loads(MedalView().get_all_medals(request).content)
    medal_nations=json.loads(MedalView().get_all_medals_by_nation(request).content)
    hosts = json.loads(HostView().get_all_hosts(request).content)

    paginator = Paginator(medals, 12)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'features/medal.html', {'page_obj': page_obj,'medal_nations': medal_nations,'athletes': athletes, 'hosts': hosts})


@csrf_exempt
def search_medal(request):
    string_searchbar = request.GET.get('string_searchbar')
    nation = request.GET.get('nation')
    gender = request.GET.get('gender')

    medals = json.loads(MedalView().search_medal(request,string_searchbar, nation, gender).content)
    athletes = json.loads(AthleteView().get_all_athletes(request).content)
    hosts = json.loads(HostView().get_all_hosts(request).content)
    medal_nations=json.loads(MedalView().get_all_medals_by_nation(request).content)


    paginator = Paginator(medals, 12)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
   
    return render(request, 'features/medal.html', {'page_obj': page_obj,'medal_nations': medal_nations,'athletes': athletes, 'hosts': hosts}) #'athletes': athletes,


@csrf_exempt
def create_medal(request): 
    if request.method == 'POST':
        data = {
            'discipline_title': request.POST.get('discipline_title_create',''),
            'slug_game': request.POST.get('slug_game_create',''),
            'event_title': request.POST.get('event_title_create',''),
            'event_gender': request.POST.get('event_gender_create',''),
            'medal_type': request.POST.get('medal_type_create',''),
            'participant_type': request.POST.get('participant_type_create',''),
            'participant_title': request.POST.get('participant_title_create',''),
            'athlete_url': request.POST.get('athlete_url_create',''),
            'athlete_full_name': request.POST.get('athlete_full_name_create',''),
            'country_name': request.POST.get('country_name_create',''),
            'country_code': request.POST.get('country_code_create',''),
            'country_3_letter_code': request.POST.get('country_3_letter_code_create',''),
        }
        medal_view = MedalView()
        medal_view.create_medal(data).content

        url = reverse('medaglie')
        response = HttpResponseRedirect(url)
        response.set_cookie('messaggio', 'Medaglia Creata')
        response.set_cookie('codice_messaggio', '200')
        return response
    
    return HttpResponse(status=405)

@csrf_exempt
def update_medal(request): 
    if request.method == 'POST':
        data = {
            '_id': request.POST.get('medal_id_update',''),
            'discipline_title': request.POST.get('discipline_title_update',''),
            'slug_game': request.POST.get('slug_game_update',''),
            'event_title': request.POST.get('event_title_update',''),
            'event_gender': request.POST.get('event_gender_update',''),
            'medal_type': request.POST.get('medal_type_update',''),
            'participant_type': request.POST.get('participant_type_update',''),
            'participant_title': request.POST.get('participant_title_update',''),
            'athlete_url': request.POST.get('athlete_url_update',''),
            'athlete_full_name': request.POST.get('athlete_full_name_update',''),
            'country_name': request.POST.get('country_name_update',''),
            'country_code': request.POST.get('country_code_update',''),
            'country_3_letter_code': request.POST.get('country_3_letter_code_update',''),
        }

        medal_view = MedalView()
        medal_view.update_medal(data).content
     
        url = reverse('medaglie')
        response = HttpResponseRedirect(url)
        response.set_cookie('messaggio', 'Medaglia Aggiornata')
        response.set_cookie('codice_messaggio', '200')
        return response
    
    return HttpResponse(status=405)


@csrf_exempt
def delete_medal(request):
    if request.method == 'POST':
        medal_id = request.POST.get('medal_id_delete')
        medal_view = MedalView()
        #delete_athlete_message = 
        medal_view.delete_medal(request, medal_id).content

        # Esegui il reindirizzamento alla vista di destinazione
        #return redirect('atleti')
        url = reverse('medaglie')
        response = HttpResponseRedirect(url)
        response.set_cookie('messaggio', 'Medaglia Eliminata')
        response.set_cookie('codice_messaggio', '200')
        return response
    
    return HttpResponse(status=405)

def result(request):
    results = json.loads(ResultView().get_all_results(request).content)
    hosts = json.loads(HostView().get_all_hosts(request).content)
    
    paginator = Paginator(results, 12)  # 10 host per pagina

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'features/result.html', {'page_obj': page_obj, 'hosts': hosts}) #'results': results,

def search_result(request):
    string_searchbar = request.GET.get('string_searchbar')
    results = json.loads(ResultView().search_results(request, string_searchbar).content)  # Decodifica del JSON
    hosts = json.loads(HostView().get_all_hosts(request).content)

    paginator = Paginator(results, 12)  # 10 atleti per pagina

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
   
    
    return render(request, 'features/result.html', {'page_obj': page_obj, 'hosts': hosts}) #'athletes': athletes,

@csrf_exempt
def create_result(request): 
    if request.method == 'POST':
        data = {
            'discipline_title': request.POST.get('discipline_title_create',''),
            'event_title': request.POST.get('event_title_create',''),
            'slug_game': request.POST.get('slug_game_create',''),
            'participant_type': request.POST.get('participant_type_create',''),
            'rank_equal': request.POST.get('rank_equal_create',''),
            'rank_position': request.POST.get('rank_position_create',''),
            'country_name': request.POST.get('country_name_create',''),
        }
        result_view = ResultView()
        result_view.create_result(data).content

        url = reverse('risultati')
        response = HttpResponseRedirect(url)
        response.set_cookie('messaggio', 'risultato aggiornato')
        response.set_cookie('codice_messaggio', '200')
        return response
    
    return HttpResponse(status=405)

@csrf_exempt
def update_result(request):  
    if request.method == 'POST':
        data = {
            '_id': request.POST.get('result_id_update',''),
            'discipline_title': request.POST.get('discipline_title_update',''),
            'event_title': request.POST.get('event_title_update',''),
            'slug_game': request.POST.get('slug_game_update',''),
            'participant_type': request.POST.get('participant_type_update',''),
            'rank_equal': request.POST.get('rank_equal_update',''),
            'rank_position': request.POST.get('rank_position_update',''),
            'country_name': request.POST.get('country_name_update','')
        }

        result_view = ResultView()
        result_view.update_result(data).content
     
        url = reverse('risultati')
        response = HttpResponseRedirect(url)
        response.set_cookie('messaggio', 'Risultato aggiornato')
        response.set_cookie('codice_messaggio', '200')
        return response
    
    return HttpResponse(status=405)

@csrf_exempt
def delete_result(request):
    if request.method == 'POST':
        result_id = request.POST.get('result_id_delete')
        result_view = ResultView()
        #delete_athlete_message = 
        result_view.delete_result(request, result_id).content

        # Esegui il reindirizzamento alla vista di destinazione
        url = reverse('risultati')
        response = HttpResponseRedirect(url)
        response.set_cookie('messaggio', 'Risultato Eliminato')
        response.set_cookie('codice_messaggio', '200')
        return response
    
    return HttpResponse(status=405)


def placing(request):

    return render(request, 'features/placing.html')

@csrf_exempt
def search_placing(request):
    string_searchbar = request.GET.get('string_searchbar')
    nation = request.GET.get('nation')
    gender = request.GET.get('gender')

    medals = json.loads(MedalView().search_medal(request,string_searchbar, nation, gender).content)
    athletes = json.loads(AthleteView().get_all_athletes(request).content)
    hosts = json.loads(HostView().get_all_hosts(request).content)
    medal_nations=json.loads(MedalView().get_all_medals_by_nation(request).content)


    paginator = Paginator(medals, 12)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
   
    return render(request, 'features/medal.html', {'page_obj': page_obj,'medal_nations': medal_nations,'athletes': athletes, 'hosts': hosts}) #'athletes': athletes,

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