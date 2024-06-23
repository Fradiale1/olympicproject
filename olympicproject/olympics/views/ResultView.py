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
            athletes_names=''
            result_athletes = result.get('athletes','')
            if(result_athletes != ''):
                athletes_list = eval(result_athletes)
                athletes_names = [athlete[0] for athlete in athletes_list]
            result_data = {
                'id': str(result['_id']),  # Converti ObjectId in stringa per JSON
                'discipline_title': str(result.get('discipline_title','')),  # Utilizza get per evitare KeyError
                'country_name': result.get('country_name',''), # Utilizza get per evitare KeyError
                'athlet': athletes_names,  # Utilizza get per evitare KeyError
                'medal_type': result.get('medal_type','')  # Utilizza get per evitare KeyError
            }
            data.append(result_data)
        return JsonResponse(data, safe=False)


    @request_mapping("/getById/<str:result_id>", method="get") #@get("/{result_id}")
    def get_result_by_id(self, request, result_id):
        result = self.result_repository.get_result_by_id(result_id)
        athletes_names=''
        result_athletes = result.get('athletes','')
        if(result_athletes != ''):
            athletes_list = eval(result_athletes)
            athletes_names = [athlete[0] for athlete in athletes_list]
        data = {
                'id': str(result['_id']),  # Converti ObjectId in stringa per JSON
                'discipline_title': str(result.get('discipline_title','')),  # Utilizza get per evitare KeyError
                'country_name': result.get('country_name',''), # Utilizza get per evitare KeyError
                'athlet': athletes_names,  # Utilizza get per evitare KeyError
                'medal_type': result.get('medal_type','')  # Utilizza get per evitare KeyError
            }
        return JsonResponse(data)

    @request_mapping("/create/", method="post")
    def create_result(self, request):
        data = request.POST
        result = self.result_repository.create_result(data.get('athlete'), data.get('event'), data.get('performance'), data.get('rank'))
        return JsonResponse({"id": str(result._id), "athlete": str(result.athlete), "event": result.event, "performance": result.performance, "rank": result.rank})

    @request_mapping("/update/<uuid:result_id>", method="post")
    def update_result(self, request, result_id):
        data = request.POST
        result = self.result_repository.update_result(result_id, data.get('athlete'), data.get('event'), data.get('performance'), data.get('rank'))
        return JsonResponse({"id": str(result._id), "athlete": str(result.athlete), "event": result.event, "performance": result.performance, "rank": result.rank})

    @request_mapping("/delete/<uuid:result_id>", method="get")
    def delete_result(self, request, result_id):
        self.result_repository.delete_result(result_id)
        return JsonResponse({"message": "Result deleted"})
