from django.http import JsonResponse
from django.views import View
from olympics.repository.HostRepository import HostRepository
from django_request_mapping import request_mapping

@request_mapping("/hosts")
class HostView(View):

    def __init__(self):
        super().__init__()
        self.host_repository: HostRepository = HostRepository(
            db_url='mongodb://localhost:27017/',  # Inserisci l'URL del tuo database MongoDB
            db_name='Olympic'  # Inserisci il nome del tuo database MongoDB
        )

    @request_mapping("/getAll", method="get")
    def get_all_hosts(self, request):
        hosts = self.host_repository.get_all_hosts()
        
        data = []
        for host in hosts:

            host_data = {
                'id': str(host['_id']),
                'game_slug': host.get('game_slug',''),
                'game_end_date': host.get('game_end_date',''),
                'game_start_date': host.get('game_start_date',''),
                'game_location': host.get('game_location',''),
                'game_name': host.get('game_name', ''),
                'game_season': host.get('game_season', ''),
                'game_year': host.get('game_year', '')
            }
            data.append(host_data)

        return JsonResponse(data, safe=False)

    @request_mapping("/getById/<str:host_id>", method="get") #@get("/{host_id}")
    def get_host_by_id(self, request, host_id):
        host = self.host_repository.get_host_by_id(host_id)
        data = {
                'id': str(host['_id']),
                'game_slug': host.get('game_slug',''),
                'game_end_date': host.get('game_end_date',''),
                'game_start_date': host.get('game_start_date',''),
                'game_location': host.get('game_location',''),
                'game_name': host.get('game_name', ''),
                'game_season': host.get('game_season', ''),
                'game_year': host.get('game_year', '')
            }
        return JsonResponse(data)

    @request_mapping("/create", method="post")
    def create_host(self, request):
        data = request.POST
        host = self.host_repository.create_host(
            data.get('game_slug'),
            data.get('game_end_date'),
            data.get('game_start_date'),
            data.get('game_location'),
            data.get('game_name'),
            data.get('game_season'),
            data.get('game_year')
        )
        return JsonResponse({
            "id": str(host['_id']),
            'game_slug': host.get('game_slug',''),
            'game_end_date': host.get('game_end_date',''),
            'game_start_date': host.get('game_start_date',''),
            'game_location': host.get('game_location',''),
            'game_name': host.get('game_name', ''),
            'game_season': host.get('game_season', ''),
            'game_year': host.get('game_year', '')
        })

    @request_mapping("/update/<str:host_id>", method="post")
    def update_host(self, request, host_id):
        data = request.POST
        host = self.host_repository.update_host(
            host_id, 
            data.get('game_slug'),
            data.get('game_end_date'),
            data.get('game_start_date'),
            data.get('game_location'),
            data.get('game_name'),
            data.get('game_season'),
            data.get('game_year')
        )
        return JsonResponse({
            "id": str(host['_id']), 
            'game_slug': host.get('game_slug',''),
            'game_end_date': host.get('game_end_date',''),
            'game_start_date': host.get('game_start_date',''),
            'game_location': host.get('game_location',''),
            'game_name': host.get('game_name', ''),
            'game_season': host.get('game_season', ''),
            'game_year': host.get('game_year', '')
        })

    @request_mapping("/delete/<str:host_id>", method="get")
    def delete_host(self, request, host_id):
        self.host_repository.delete_host(host_id)
        return JsonResponse({"message": "Città ospite eliminata"})