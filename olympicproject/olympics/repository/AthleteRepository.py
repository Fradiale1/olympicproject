from pymongo import MongoClient, ReturnDocument
from bson.objectid import ObjectId

class AthleteRepository:
    def __init__(self, db_url, db_name):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.athletes_collection = self.db['athletes']

    def get_all_athletes(self):
        return list(self.athletes_collection.find())

    def get_athlete_by_id(self, athlete_id):
        return self.athletes_collection.find_one({'_id': ObjectId(athlete_id)})

    def create_athlete(self, name, sport, age):
        athlete = {
            'name': name,
            'sport': sport,
            'age': age
        }
        result = self.athletes_collection.insert_one(athlete)
        athlete['_id'] = result.inserted_id
        return athlete

    def update_athlete(self, athlete_id, name=None, sport=None, age=None):
        update_fields = {}
        if name:
            update_fields['name'] = name
        if sport:
            update_fields['sport'] = sport
        if age:
            update_fields['age'] = age
        
        result = self.athletes_collection.find_one_and_update(
            {'_id': ObjectId(athlete_id)},
            {'$set': update_fields},
            return_document=ReturnDocument.AFTER
        )
        return result

    def delete_athlete(self, athlete_id):
        result = self.athletes_collection.delete_one({'_id': ObjectId(athlete_id)})
        return result.deleted_count > 0
