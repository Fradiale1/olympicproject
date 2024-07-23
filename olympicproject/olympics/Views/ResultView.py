from django.http import JsonResponse
from django.views import View
from olympics.repository.ResultRepository import ResultRepository
from django_request_mapping import request_mapping

@request_mapping("/results")
class ResultView(View):

    def __init__(self):
        super().__init__()
        self.result_repository: ResultRepository = ResultRepository(
            db_url='mongodb://localhost:27017/',  # Inserisci l'URL del tuo database MongoDB
            db_name='Olympic'  # Inserisci il nome del tuo database MongoDB
        )

    @request_mapping("/getAll", method="get")
    def get_all_results(self, request):
        results = self.result_repository.get_all_results()
        data = []
        for result in results:
            result_data = {
                'id': str(result['_id']),
                'discipline_title': result.get('discipline_title',''),
                'rank_position': result.get('rank_position',''),
                'country_name': result.get('country_name',''),
                'event_title': result.get('event_title',''),
                'slug_game': result.get('slug_game','')
            }
                #'event_title': result.get('event_title',''),
                #'slug_game': result.get('slug_game',''),
                #'participant_type': result.get('participant_type',''),
                #'medal_type': result.get('medal_type',''),
                #'rank_equal': result.get('rank_equal',''),
                #'athletes': athletes_names,
                #'country_code': result.get('country_code',''),
                #'country_3_letter_code': result.get('country_3_letter_code','')
            data.append(result_data)

        return JsonResponse(data, safe=False)
    
    @request_mapping("/search/<str:string>", method="get")
    def search_results(self, request, string):
        results = self.result_repository.search_results(string)
        #year = int(datetime.date.today().strftime("%Y"))
        
        data = []
        for result in results:
            #athlet_age = athlete.get('athlete_year_birth', '')
            #if(athlet_age != ''):
            #    athlet_age = int(year) - athlet_age

            result_data = {
                'id': str(result['_id']),
                'discipline_title': result.get('discipline_title',''),
                'rank_position': result.get('rank_position',''),
                'country_name': result.get('country_name',''),
                'event_title': result.get('event_title',''),
                'slug_game': result.get('slug_game',''),
                'rank_position':result.get('rank_position','')
            }
                
                
                #'participant_type': result.get('participant_type',''),
                #'medal_type': result.get('medal_type',''),
                #'rank_equal': result.get('rank_equal',''),
                #'athletes': athletes_names,
                #'country_code': result.get('country_code',''),
                #'country_3_letter_code': result.get('country_3_letter_code','')
            data.append(result_data)

        return JsonResponse(data, safe=False)

    @request_mapping("/getById/<str:result_id>", method="get") #@get("/{result_id}")
    def get_result_by_id(self, request, result_id):
        result = self.result_repository.get_result_by_id(result_id)
        data = {
                'id': str(result['_id']),
                'discipline_title': result.get('discipline_title',''),
                'event_title': result.get('event_title',''),
                'slug_game': result.get('slug_game',''),
                'participant_type': result.get('participant_type',''),
                'medal_type': result.get('medal_type',''),
                #'athletes': athletes_names,
                'rank_equal': result.get('rank_equal',''),
                'rank_position': result.get('rank_position',''),
                'country_name': result.get('country_name',''),
                #'country_code': result.get('country_code',''),
                #'country_3_letter_code': result.get('country_3_letter_code','')
            }
        return JsonResponse(data)

    @request_mapping("/create", method="post")
    def create_result(self, requestData):
        data = requestData
        result = self.result_repository.create_result(
            data.get('discipline_title'),
            data.get('event_title'),
            data.get('slug_game'),
            data.get('participant_type'),
            data.get('medal_type'),
            #data.get('athletes'),
            data.get('rank_equal'),
            data.get('rank_position'),
            data.get('country_name')
            #data.get('country_code'),
            #data.get('country_3_letter_code')
        )
        return JsonResponse({
            "id": str(result['_id']),
            "discipline_title": result.get('discipline_title',''),
            "event_title": result.get('event_title',''),
            "slug_game": result.get('slug_game',''),
            "participant_type": result.get('participant_type',''),
            'medal_type': result.get('medal_type',''),
            #'athletes': result.get('athletes',''),
            "rank_equal": result.get('rank_equal',''),
            "rank_position": result.get('rank_position',''),
            "country_name": result.get('country_name','')
            #'country_code': result.get('country_code',''),
            #'country_3_letter_code': result.get('country_3_letter_code','')
        })

    @request_mapping("/update/<str:result_id>", method="post")
    def update_result(self, requestData):
        data = requestData
        result = self.result_repository.update_result(
            data.get('_id'),
            data.get('discipline_title'),
            data.get('event_title'),
            data.get('slug_game'),
            data.get('participant_type'),
            data.get('medal_type'),
            #data.get('athletes'),
            data.get('rank_equal'),
            data.get('rank_position'),
            data.get('country_name'),
            #data.get('country_code'),
            #data.get('country_3_letter_code')
        )
        return JsonResponse({
            'id': str(result['_id']),
            'discipline_title': result.get('discipline_title',''),
            'event_title': result.get('event_title',''),
            'slug_game': result.get('slug_game',''),
            'participant_type': result.get('participant_type',''),
            'medal_type': result.get('medal_type',''),
            #'athletes': result.get('athletes',''),
            'rank_equal': result.get('rank_equal',''),
            'rank_position': result.get('rank_position',''),
            'country_name': result.get('country_name',''),
            #'country_code': result.get('country_code',''),
            #'country_3_letter_code': result.get('country_3_letter_code','')
        })

    @request_mapping("/delete/<str:result_id>", method="get")
    def delete_result(self, request, result_id):
        self.result_repository.delete_result(result_id)
        return JsonResponse({"message": "Resultato eliminato"})

    @request_mapping("/getAll_by_discipline", method="get")
    def get_all_results_by_discipline(self, request):
        results = self.result_repository.get_all_results_by_discipline()
        data = []
        for result in results:
            result_data = {
                'id': str(result['_id']),
                'discipline_title': result.get('discipline_title',''),
                'slug_game': result.get('slug_game',''),
                'event_title': result.get('event_title',''),
                'rank_position': result.get('rank_position',''),
                'country_name': result.get('country_name','')
            }
            data.append(result_data)
        return JsonResponse(data, safe=False)
    
    @request_mapping("/getAll_by_event", method="get")
    def get_all_results_by_event(self, request):
        results = self.result_repository.get_all_results_by_event()
        data = []
        for result in results:
            result_data = {
                'id': str(result['_id']),
                'discipline_title': result.get('discipline_title',''),
                'slug_game': result.get('slug_game',''),
                'event_title': result.get('event_title',''),
                'rank_position': result.get('rank_position',''),
                'country_name': result.get('country_name','')
            }
            data.append(result_data)
        return JsonResponse(data, safe=False)
    
    @request_mapping("/getAll_by_sluggame", method="get")
    def get_all_results_by_sluggame(self, request):
        results = self.result_repository.get_all_results_by_olimpiade()
        data = []
        for result in results:
            result_data = {
                'id': str(result['_id']),
                'discipline_title': result.get('discipline_title',''),
                'slug_game': result.get('slug_game',''),
                'event_title': result.get('event_title',''),
                'rank_position': result.get('rank_position',''),
                'country_name': result.get('country_name','')
            }
            data.append(result_data)
        return JsonResponse(data, safe=False)
    

    @request_mapping("/search_placing/<str:string>", method="get")
    def search_placing(self, request, discipline, event, olimpiade):
        results = self.result_repository.search_placing(discipline, event, olimpiade)

        data = []
        for result in results:
            result_data = {
                'id': str(result['_id']),
                'discipline_title': result.get('discipline_title',''),
                'slug_game': result.get('slug_game',''),
                'event_title': result.get('event_title',''),
                'rank_position': result.get('rank_position',''),
                'country_name': result.get('country_name',''),
            }
            data.append(result_data)

        return JsonResponse(data, safe=False)