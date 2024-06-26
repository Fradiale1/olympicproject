from pymongo import MongoClient, ReturnDocument
from bson.objectid import ObjectId

class ResultRepository:
    def __init__(self, db_url, db_name):
        self.client = MongoClient(db_url)
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

    def create_result(self, discipline_title, event_title, slug_game, participant_type, medal_type, athletes, rank_equal, rank_position, country_name, country_code, country_3_letter_code):
        result = {
            'discipline_title': discipline_title,
            'event_title': event_title,
            'slug_game': slug_game,
            'participant_type': participant_type,
            'medal_type': medal_type,
            'athletes': athletes,
            'rank_equal': rank_equal,
            'rank_position': rank_position,
            'country_name': country_name,
            'country_code': country_code,
            'country_3_letter_code': country_3_letter_code
        }
        
        try:
            result = self.results_collection.insert_one(result)
            result['_id'] = result.inserted_id
            return result
        except Exception as e:
            print(f"Errore nel creare il risultato: {e}")
            return None

    def update_result(self, result_id, discipline_title, event_title, slug_game, participant_type, medal_type, athletes, rank_equal, rank_position, country_name, country_code, country_3_letter_code):
        update_fields = {}
        if discipline_title:
            update_fields['discipline_title'] = discipline_title
        if event_title:
            update_fields['event_title'] = event_title
        if slug_game:
            update_fields['slug_game'] = slug_game
        if participant_type:
            update_fields['participant_type'] = participant_type
        if medal_type:
            update_fields['medal_type'] = medal_type
        if athletes:
            update_fields['athletes'] = athletes
        if rank_equal:
            update_fields['rank_equal'] = rank_equal
        if rank_position:
            update_fields['rank_position'] = rank_position
        if country_name:
            update_fields['country_name'] = country_name
        if country_code:
            update_fields['country_code'] = country_code
        if country_3_letter_code:
            update_fields['country_3_letter_code'] = country_3_letter_code

        try:
            result = self.results_collection.find_one_and_update(
                {'_id': ObjectId(result_id)},
                {'$set': update_fields},
                return_document=ReturnDocument.AFTER
            )
            return result
        except Exception as e:
            print(f"Errore nel aggiornare il risultato con ID {result_id}: {e}")
            return None

    def delete_result(self, result_id):
        try:
            result = self.results_collection.delete_one({'_id': ObjectId(result_id)})
            return result.deleted_count > 0
        except Exception as e:
            print(f"Errore nel cancellare il risultato con ID {result_id}: {e}")
            return False