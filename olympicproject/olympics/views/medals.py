# olympics/views.py

from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from ..models import Medal

def medal_list(request):
    medals = Medal.objects.all()
    data = {
        'medals': list(medals.values())
    }
    return JsonResponse(data)

def medal_detail(request, medal_id):
    medal = get_object_or_404(Medal, id=medal_id)
    data = {
        'medal': {
            'id': medal.id,
            'discipline_title': medal.discipline_title,
            'slug_game': medal.slug_game,
            'event_title': medal.event_title,
            'event_gender': medal.event_gender,
            'medal_type': medal.medal_type,
            'participant_type': medal.participant_type,
            'participant_title': medal.participant_title,
            'athlete_url': medal.athlete_url,
            'athlete_full_name': medal.athlete_full_name,
            'country_name': medal.country_name,
            'country_code': medal.country_code,
            'country_3_letter_code': medal.country_3_letter_code
        }
    }
    return JsonResponse(data)
