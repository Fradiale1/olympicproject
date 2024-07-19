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
        
    def search_results(self, search_query):
        try:
            # Utilizziamo il regex per cercare la stringa parziale in tutti i campi
            query = {
                '$or': [
                    {'discipline_title': {'$regex': search_query, '$options': 'i'}},
                    {'event_title': {'$regex': search_query, '$options': 'i'}},
                    {'slug_game': {'$regex': search_query, '$options': 'i'}},
                    {'participant_type': {'$regex': search_query, '$options': 'i'}},
                    {'medal_type': {'$regex': search_query, '$options': 'i'}},
                    {'rank_equal': {'$regex': search_query, '$options': 'i'}},
                    {'rank_position': {'$regex': search_query, '$options': 'i'}},
                    {'country_name': {'$regex': search_query, '$options': 'i'}},
                ]
            }
            results = list(self.results_collection.find(query).limit(200))
            return results
        except Exception as e:
            print(f"Errore nella ricerca dei risultati per '{search_query}': {e}")
            return []

    def create_result(self, discipline_title, event_title, slug_game, participant_type, medal_type, rank_equal, rank_position, country_name):
        if rank_position == "1" :
            result = {
                'discipline_title': discipline_title,
                'event_title': event_title,
                'slug_game': slug_game,
                'participant_type': participant_type,
                'medal_type': 'GOLD',
                #'athletes': athletes,
                'rank_equal': rank_equal,
                'rank_position': rank_position,
                'country_name': country_name,
                #'country_code': country_code,
                #'country_3_letter_code': country_3_letter_code
            }

        elif rank_position == "2" :
            result = {
                'discipline_title': discipline_title,
                'event_title': event_title,
                'slug_game': slug_game,
                'participant_type': participant_type,
                'medal_type': 'SILVER',
                #'athletes': athletes,
                'rank_equal': rank_equal,
                'rank_position': rank_position,
                'country_name': country_name,
                #'country_code': country_code,
                #'country_3_letter_code': country_3_letter_code
            }

        elif rank_position == "3" :
            result = {
                'discipline_title': discipline_title,
                'event_title': event_title,
                'slug_game': slug_game,
                'participant_type': participant_type,
                'medal_type': 'BRONZE',
                #'athletes': athletes,
                'rank_equal': rank_equal,
                'rank_position': rank_position,
                'country_name': country_name,
                #'country_code': country_code,
                #'country_3_letter_code': country_3_letter_code
            }

        else :
            result = {
                'discipline_title': discipline_title,
                'event_title': event_title,
                'slug_game': slug_game,
                'participant_type': participant_type,
                #'medal_type': 'GOLD',
                #'athletes': athletes,
                'rank_equal': rank_equal,
                'rank_position': rank_position,
                'country_name': country_name,
                #'country_code': country_code,
                #'country_3_letter_code': country_3_letter_code
            }
        
        
        try:
            result = self.results_collection.insert_one(result)
            result['_id'] = result.inserted_id
            return result
        except Exception as e:
            print(f"Errore nel creare il risultato: {e}")
            return None

    def update_result(self, result_id, discipline_title, event_title, slug_game, participant_type, medal_type, rank_equal, rank_position, country_name):
        update_fields = {}
        if discipline_title:
            update_fields['discipline_title'] = discipline_title
        if event_title:
            update_fields['event_title'] = event_title
        if slug_game:
            update_fields['slug_game'] = slug_game
        if participant_type:
            update_fields['participant_type'] = participant_type
        if rank_equal:
            update_fields['rank_equal'] = rank_equal
        if rank_position:
            update_fields['rank_position'] = rank_position
            if rank_position == "1" :
                update_fields['medal_type'] = 'GOLD'
            elif rank_position == "2" :
                update_fields['medal_type'] = 'SILVER'
            elif rank_position == "3" :
                update_fields['medal_type'] = 'BRONZE'
            else :
                update_fields['medal_type'] = ''
        if country_name:
            update_fields['country_name'] = country_name

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