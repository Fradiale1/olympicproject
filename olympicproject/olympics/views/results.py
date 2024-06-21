# olympics/views.py

from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from ..models import Result

def result_list(request):
    results = Result.objects.all()
    data = {
        'results': list(results.values())
    }
    return JsonResponse(data)

def result_detail(request, result_id):
    result = get_object_or_404(Result, id=result_id)
    data = {
        'result': {
            'id': result.id,
            'discipline_title': result.discipline_title,
            'event_title': result.event_title,
            'slug_game': result.slug_game,
            'participant_type': result.participant_type,
            'medal_type': result.medal_type,
            'athletes': result.athletes,
            'rank_equal': result.rank_equal,
            'rank_position': result.rank_position,
            'country_name': result.country_name,
            'country_code': result.country_code,
            'country_3_letter_code': result.country_3_letter_code
        }
    }
    return JsonResponse(data)
