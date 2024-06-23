from pymongo import MongoClient, ReturnDocument
from bson.objectid import ObjectId

class AthleteRepository:
    def __init__(self, db_url, db_name):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.athletes_collection = self.db['athletes']

    def get_all_athletes(self):
        try:
            return list(self.athletes_collection.find())
        except Exception as e:
            print(f"Errore nel recuperare tutti gli atleti: {e}")
            return []

    def get_athlete_by_id(self, athlete_id):
        try:
            return self.athletes_collection.find_one({'_id': ObjectId(athlete_id)})
        except Exception as e:
            print(f"Errore nel recuperare l'atleta con ID {athlete_id}: {e}")
            return None

    def create_athlete(self, name, sport, age):
        athlete = {
            'name': name,
            'sport': sport,
            'age': age
        }
        try:
            result = self.athletes_collection.insert_one(athlete)
            athlete['_id'] = result.inserted_id
            return athlete
        except Exception as e:
            print(f"Errore nel creare l'atleta: {e}")
            return None

    def update_athlete(self, athlete_id, name=None, sport=None, age=None):
        update_fields = {}
        if name:
            update_fields['name'] = name
        if sport:
            update_fields['sport'] = sport
        if age:
            update_fields['age'] = age

        try:
            result = self.athletes_collection.find_one_and_update(
                {'_id': ObjectId(athlete_id)},
                {'$set': update_fields},
                return_document=ReturnDocument.AFTER
            )
            return result
        except Exception as e:
            print(f"Errore nel aggiornare l'atleta con ID {athlete_id}: {e}")
            return None

    def delete_athlete(self, athlete_id):
        try:
            result = self.athletes_collection.delete_one({'_id': ObjectId(athlete_id)})
            return result.deleted_count > 0
        except Exception as e:
            print(f"Errore nel cancellare l'atleta con ID {athlete_id}: {e}")
            return False
