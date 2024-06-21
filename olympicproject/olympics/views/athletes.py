# olympics/views_athletes.py

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import Athlete

# Views per il modello Athlete
def athlete_list(request):
    athletes = Athlete.objects.all()
    data = {
        'athletes': list(athletes.values())
    }
    return JsonResponse(data)

def athlete_detail(request, athlete_id):
    athlete = get_object_or_404(Athlete, id=athlete_id)
    data = {
        'athlete': {
            'id': athlete.id,
            'athlete_url': athlete.athlete_url,
            'athlete_full_name': athlete.athlete_full_name,
            'games_participations': athlete.games_participations,
            'first_game': athlete.first_game,
            'athlete_year_birth': athlete.athlete_year_birth
        }
    }
    return JsonResponse(data)
