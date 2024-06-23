from olympics.models import Medal
from bson import ObjectId
import pymongo
from django.http import JsonResponse

class MedalRepository:
    def __init__(self, db_url, db_name):
        self.client = pymongo.MongoClient(db_url)
        self.db = self.client[db_name]
        self.medals_collection = self.db['medals']

    def get_all_medals(self):
        return list(self.medals_collection.find())

    def get_medal_by_id(self, medal_id):
        try:
            return self.medals_collection.find_one({'_id': ObjectId(medal_id)})
        except Exception as e:
            print(f"Errore: {e}")
            return None

    def create_medal(self, data):
        result = self.medals_collection.insert_one(data)
        return result.inserted_id

    def update_medal(self, medal_id, data):
        result = self.medals_collection.update_one(
            {'_id': ObjectId(medal_id)},
            {'$set': data}
        )
        return result.modified_count > 0

    def delete_medal(self, medal_id):
        result = self.medals_collection.delete_one({'_id': ObjectId(medal_id)})
        return result.deleted_count > 0
