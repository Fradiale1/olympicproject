from django.http import JsonResponse
from django.views import View
from olympics.repository.MedalRepository import MedalRepository
from django_request_mapping import request_mapping

@request_mapping("/medals")
class MedalView(View):

    def __init__(self):
        super().__init__()
        self.medal_repository: MedalRepository = MedalRepository(
            db_url='mongodb://localhost:27017/',  # Inserisci l'URL del tuo database MongoDB
            db_name='Olympic'  # Inserisci il nome del tuo database MongoDB
        )

    @request_mapping("/getAll", method="get")
    def get_all_medals(self, request):
        medals = self.medal_repository.get_all_medals()
        data = []
        for medal in medals:
            medal_data = {
                'id': str(medal['_id']),  # Converti ObjectId in stringa per JSON
                'medal_type': medal.get('medal_type',''),  # Utilizza get per evitare KeyError
                'athlete_full_name': medal.get('athlete_full_name',''),  # Utilizza get per evitare KeyError
                'country_name': medal.get('country_name','')  # Utilizza get per evitare KeyError
            }
            data.append(medal_data)
        return JsonResponse(data, safe=False)


    @request_mapping("/getById/<str:medal_id>", method="get") #@get("/{medal_id}")
    def get_medal_by_id(self, request, medal_id):
        medal = self.medal_repository.get_medal_by_id(medal_id)
        data = {
                'id': str(medal['_id']),  # Converti ObjectId in stringa per JSON
                'medal_type': medal.get('medal_type',''),  # Utilizza get per evitare KeyError
                'athlete_full_name': medal.get('athlete_full_name',''),  # Utilizza get per evitare KeyError
                'country_name': medal.get('country_name','')  # Utilizza get per evitare KeyError
            }
        return JsonResponse(data)

    @request_mapping("/create/", method="post")
    def create_medal(self, request):
        data = request.POST
        medal = self.medal_repository.create_medal(data.get('athlete'), data.get('event'), data.get('medal_type'))
        return JsonResponse({"id": str(medal._id), "athlete": str(medal.athlete), "event": medal.event, "medal_type": medal.medal_type})

    @request_mapping("/update/<str:medal_id>", method="post")
    def update_medal(self, request, medal_id):
        data = request.POST
        medal = self.medal_repository.update_medal(medal_id, data.get('athlete'), data.get('event'), data.get('medal_type'))
        return JsonResponse({"id": str(medal._id), "athlete": str(medal.athlete), "event": medal.event, "medal_type": medal.medal_type})

    @request_mapping("/delete/<str:medal_id>", method="get")
    def delete_medal(self, request, medal_id):
        self.medal_repository.delete_medal(medal_id)
        return JsonResponse({"message": "Medal deleted"})