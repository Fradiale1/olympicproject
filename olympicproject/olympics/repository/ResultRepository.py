from olympics.models import Result
from bson import ObjectId
import pymongo
from django.http import JsonResponse

class ResultRepository:
    def __init__(self, db_url, db_name):
        self.client = pymongo.MongoClient(db_url)
        self.db = self.client[db_name]
        self.results_collection = self.db['results']

    def get_all_results(self):
        try:
            return list(self.results_collection.find())
        except Exception as e:
            print(f"Errore nel recuperare tutti i risultati: {e}")
            return []

    def get_result_by_id(self, result_id):
        try:
            return self.results_collection.find_one({'_id': ObjectId(result_id)})
        except Exception as e:
            print(f"Errore nel recuperare il risultato con ID {result_id}: {e}")
            return None

    def create_result(self, data):
        try:
            result = self.results_collection.insert_one(data)
            return result.inserted_id
        except Exception as e:
            print(f"Errore nel creare il risultato: {e}")
            return None

    def update_result(self, result_id, data):
        try:
            result = self.results_collection.update_one(
                {'_id': ObjectId(result_id)},
                {'$set': data}
            )
            return result.modified_count > 0
        except Exception as e:
            print(f"Errore nel aggiornare il risultato con ID {result_id}: {e}")
            return False

    def delete_result(self, result_id):
        try:
            result = self.results_collection.delete_one({'_id': ObjectId(result_id)})
            return result.deleted_count > 0
        except Exception as e:
            print(f"Errore nel cancellare il risultato con ID {result_id}: {e}")
            return False