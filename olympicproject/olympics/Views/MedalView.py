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
                'id': str(medal['_id']),
                'discipline_title': medal.get('discipline_title',''),
                'slug_game': medal.get('slug_game',''),
                'event_title': medal.get('event_title',''),
                'event_gender': medal.get('event_gender',''),
                'medal_type': medal.get('medal_type',''),
                'participant_type': medal.get('participant_type',''),
                'participant_title': medal.get('participant_title',''),
                'athlete_full_name': medal.get('athlete_full_name',''),
                'country_name': medal.get('country_name',''),
                'country_code': medal.get('country_code',''),
                'country_3_letter_code': medal.get('country_3_letter_code','')
            }
                #'athlete_url': medal.get('athlete_url',''),
            data.append(medal_data)
        return JsonResponse(data, safe=False)
    
    @request_mapping("/getAll_by_nation", method="get")
    def get_all_medals_by_nation(self, request):
        medals = self.medal_repository.get_all_medals_by_nation()
        data = []
        for medal in medals:
            medal_data = {
                'id': str(medal['_id']),
                'discipline_title': medal.get('discipline_title',''),
                'slug_game': medal.get('slug_game',''),
                'event_title': medal.get('event_title',''),
                'event_gender': medal.get('event_gender',''),
                'medal_type': medal.get('medal_type',''),
                'participant_type': medal.get('participant_type',''),
                'participant_title': medal.get('participant_title',''),
                'athlete_full_name': medal.get('athlete_full_name',''),
                'country_name': medal.get('country_name',''),
                'country_code': medal.get('country_code',''),
                'country_3_letter_code': medal.get('country_3_letter_code','')
            }
                #'athlete_url': medal.get('athlete_url',''),
            data.append(medal_data)
        return JsonResponse(data, safe=False)


    @request_mapping("/filter_nation/<str:string>", method="get")
    def filter_by_nation(self, request, string):
        medals = self.medal_repository.filter_by_nation(string)
        #year = int(datetime.date.today().strftime("%Y"))
        
        data = []
        for medal in medals:
            #athlet_age = athlete.get('athlete_year_birth', '')
            #if(athlet_age != ''):
            #    athlet_age = int(year) - athlet_age

            medal_data = {
                'id': str(medal['_id']),  # Converti ObjectId in stringa per JSON
                'discipline_title': medal.get('discipline_title',''),
                'slug_game': medal.get('slug_game', ''),
                'event_title': medal.get('event_title',''),
                'event_gender': medal.get('event_gender',''),
                'medal_type': medal.get('medal_type',''),
                'participant_type': medal.get('participant_type',''),
                'participant_title': medal.get('participant_title',''),
                'athlete_url': medal.get('athlete_url',''),
                'athlete_full_name': medal.get('athlete_full_name',''),
                'country_name': medal.get('country_name',''),
                'country_code': medal.get('country_code',''),
                'country_3_letter_code': medal.get('country_3_letter_code','')
            }
            data.append(medal_data)

        return JsonResponse(data, safe=False)
    

    @request_mapping("/filter_gender/<str:string>", method="get")
    def filter_by_gender(self, request, string):
        medals = self.medal_repository.filter_by_gender(string)
        #year = int(datetime.date.today().strftime("%Y"))
        
        data = []
        for medal in medals:
            #athlet_age = athlete.get('athlete_year_birth', '')
            #if(athlet_age != ''):
            #    athlet_age = int(year) - athlet_age

            medal_data = {
                'id': str(medal['_id']),  # Converti ObjectId in stringa per JSON
                'discipline_title': medal.get('discipline_title',''),
                'slug_game': medal.get('slug_game', ''),
                'event_title': medal.get('event_title',''),
                'event_gender': medal.get('event_gender',''),
                'medal_type': medal.get('medal_type',''),
                'participant_type': medal.get('participant_type',''),
                'participant_title': medal.get('participant_title',''),
                'athlete_url': medal.get('athlete_url',''),
                'athlete_full_name': medal.get('athlete_full_name',''),
                'country_name': medal.get('country_name',''),
                'country_code': medal.get('country_code',''),
                'country_3_letter_code': medal.get('country_3_letter_code','')
            }
            data.append(medal_data)

        return JsonResponse(data, safe=False)



    @request_mapping("/getById/<str:medal_id>", method="get") #@get("/{medal_id}")
    def get_medal_by_id(self, request, medal_id):
        medal = self.medal_repository.get_medal_by_id(medal_id)
        data = {
                'id': str(medal['_id']),
                'discipline_title': medal.get('discipline_title',''),
                'slug_game': medal.get('slug_game',''),
                'event_title': medal.get('event_title',''),
                'event_gender': medal.get('event_gender',''),
                'medal_type': medal.get('medal_type',''),
                'participant_type': medal.get('participant_type',''),
                'participant_title': medal.get('participant_title',''),
                'athlete_full_name': medal.get('athlete_full_name',''),
                'country_name': medal.get('country_name',''),
                'country_code': medal.get('country_code',''),
                'country_3_letter_code': medal.get('country_3_letter_code','')
            }
                #'athlete_url': medal.get('athlete_url',''),
        return JsonResponse(data)

    @request_mapping("/create", method="post")
    def create_medal(self, requestData):
        data = requestData
        medal = self.medal_repository.create_medal(
            data.get('discipline_title'),
            data.get('slug_game'),
            data.get('event_title'),
            data.get('event_gender'),
            data.get('medal_type'),
            data.get('participant_type'),
            data.get('participant_title'),
            data.get('athlete_full_name'),
            data.get('country_name'),
            data.get('country_code'),
            data.get('country_3_letter_code')
        )
            #data.get('athlete_url'),
        return JsonResponse({
            'id': str(medal['_id']),
            'discipline_title': medal.get('discipline_title',''),
            'slug_game': medal.get('slug_game',''),
            'event_title': medal.get('event_title',''),
            'event_gender': medal.get('event_gender',''),
            'medal_type': medal.get('medal_type',''),
            'participant_type': medal.get('participant_type',''),
            'participant_title': medal.get('participant_title',''),
            'athlete_full_name': medal.get('athlete_full_name',''),
            'country_name': medal.get('country_name',''),
            'country_code': medal.get('country_code',''),
            'country_3_letter_code': medal.get('country_3_letter_code','')
        })
            #'athlete_url': medal.get('athlete_url',''),

    @request_mapping("/update/<str:medal_id>", method="post")
    def update_medal(self, requestData):
        data = requestData
        medal = self.medal_repository.update_medal(
            data.get('_id'),
            data.get('discipline_title'),
            data.get('slug_game'),
            data.get('event_title'),
            data.get('event_gender'),
            data.get('medal_type'),
            data.get('participant_type'),
            data.get('participant_title'),
            data.get('athlete_full_name'),
            data.get('country_name'),
            data.get('country_code'),
            data.get('country_3_letter_code')
        )
            #data.get('athlete_url'),
        return JsonResponse({
            "id": str(medal['_id']), 
            "discipline_title": medal.get('discipline_title',''),
            "slug_game": medal.get('slug_game',''),
            "event_title": medal.get('event_title',''),
            "event_gender": medal.get('event_gender',''),
            "medal_type": medal.get('medal_type',''),
            "participant_type": medal.get('participant_type',''),
            "participant_title": medal.get('participant_title',''),
            "athlete_full_name": medal.get('athlete_full_name',''),
            "country_name": medal.get('country_name',''),
            "country_code": medal.get('country_code',''),
            "country_3_letter_code": medal.get('country_3_letter_code','')
        })
            #"athlete_url": medal.get('athlete_url',''),

    @request_mapping("/delete/<str:medal_id>", method="get")
    def delete_medal(self, request, medal_id):
        self.medal_repository.delete_medal(medal_id)
        return JsonResponse({"message": "Medaglia eliminata"})