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
        return list(self.results_collection.find())

    def get_result_by_id(self, result_id):
        return self.results_collection.find_one({'_id': ObjectId(result_id)})

    def create_result(self, data):
        result = self.results_collection.insert_one(data)
        return result.inserted_id

    def update_result(self, result_id, data):
        result = self.results_collection.update_one(
            {'_id': ObjectId(result_id)},
            {'$set': data}
        )
        return result.modified_count > 0

    def delete_result(self, result_id):
        result = self.results_collection.delete_one({'_id': ObjectId(result_id)})
        return result.deleted_count > 0
