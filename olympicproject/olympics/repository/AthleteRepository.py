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

    def create_athlete(self, athlete_url, athlete_full_name, games_partecipations, first_game, athlete_year_birth, athlete_medals, bio):
        athlete = {
            'athlete_url': athlete_url, 
            'athlete_full_name': athlete_full_name, 
            'games_partecipations': games_partecipations, 
            'first_game': first_game, 
            'athlete_year_birth': athlete_year_birth, 
            'athlete_medals': athlete_medals, 
            'bio': bio
        }
        try:
            result = self.athletes_collection.insert_one(athlete)
            athlete['id'] = result.inserted_id
            return athlete
        except Exception as e:
            print(f"Errore nel creare l'atleta: {e}")
            return None

    def update_athlete(self, athlete_id, athlete_url=None, athlete_full_name=None, games_partecipations=None, first_game=None, athlete_year_birth=None, athlete_medals=None, bio=None):
        update_fields = {}
        if athlete_url:
            update_fields['athlete_url'] = athlete_url
        if athlete_full_name:
            update_fields['athlete_full_name'] = athlete_full_name
        if games_partecipations:
            update_fields['games_partecipations'] = games_partecipations
        if first_game:
            update_fields['first_game'] = first_game
        if athlete_year_birth:
            update_fields['athlete_year_birth'] = athlete_year_birth
        if athlete_medals:
            update_fields['athlete_medals'] = athlete_medals
        if bio:
            update_fields['bio'] = bio

        try:
            result = self.athletes_collection.find_one_and_update(
                {'_id': ObjectId(athlete_id)},
                {'$set': update_fields},
                return_document=ReturnDocument.AFTER
            )
            print(result)
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
