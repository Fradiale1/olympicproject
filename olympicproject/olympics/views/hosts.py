# olympics/views.py

from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from ..models import Host

def host_list(request):
    hosts = Host.objects.all()
    data = {
        'hosts': list(hosts.values())
    }
    return JsonResponse(data)

def host_detail(request, host_id):
    host = get_object_or_404(Host, id=host_id)
    data = {
        'host': {
            'id': host.id,
            'game_slug': host.game_slug,
            'game_end_date': host.game_end_date.isoformat(),
            'game_start_date': host.game_start_date.isoformat(),
            'game_location': host.game_location,
            'game_name': host.game_name,
            'game_season': host.game_season,
            'game_year': host.game_year
        }
    }
    return JsonResponse(data)
