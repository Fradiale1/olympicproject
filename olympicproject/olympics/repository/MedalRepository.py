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
        try:
            return list(self.medals_collection.find())
        except Exception as e:
            print(f"Errore nel recuperare tutte le medaglie: {e}")
            return []

    def get_medal_by_id(self, medal_id):
        try:
            return self.medals_collection.find_one({'_id': ObjectId(medal_id)})
        except Exception as e:
            print(f"Errore nel recuperare la medaglia con ID {medal_id}: {e}")
            return None

    def create_medal(self, data):
        try:
            result = self.medals_collection.insert_one(data)
            return result.inserted_id
        except Exception as e:
            print(f"Errore nel creare la medaglia: {e}")
            return None

    def update_medal(self, medal_id, data):
        try:
            result = self.medals_collection.update_one(
                {'_id': ObjectId(medal_id)},
                {'$set': data}
            )
            return result.modified_count > 0
        except Exception as e:
            print(f"Errore nel aggiornare la medaglia con ID {medal_id}: {e}")
            return False

    def delete_medal(self, medal_id):
        try:
            result = self.medals_collection.delete_one({'_id': ObjectId(medal_id)})
            return result.deleted_count > 0
        except Exception as e:
            print(f"Errore nel cancellare la medaglia con ID {medal_id}: {e}")
            return False
