from pymongo import MongoClient, ReturnDocument
from bson.objectid import ObjectId

class MedalRepository:
    def __init__(self, db_url, db_name):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.medals_collection = self.db['medals']

    def get_all_medals(self):
        try:
            return list(self.medals_collection.find())
        except Exception as e:
            print(f"Errore nel recuperare tutte le medaglie: {e}")
            return []


    def get_all_medals_by_nation(self):
        all_medals = self.get_all_medals()
        medals_by_nation = {}
        try:
            for medal in all_medals:
                country_name = medal.get('country_name')
                if country_name:
                    if country_name not in medals_by_nation:
                        medals_by_nation[country_name] = medal
            return list(medals_by_nation.values())
        except Exception as e:
            print(f"Errore nel recuperare tutte le medaglie per nazione: {e}")
            return []

    def get_medal_by_id(self, medal_id):
        try:
            return self.medals_collection.find_one({'_id': ObjectId(medal_id)})
        except Exception as e:
            print(f"Errore nel recuperare la medaglia con ID {medal_id}: {e}")
            return None


    def search_medal(self, string, nation, gender):
        try:
            query = {
                    
                }
            
            if string:
                query['$and'] = [{'discipline_title': {'$regex': string, '$options': 'i'}}]
            
            if nation:
                 query['country_name'] = {'$regex': nation, '$options': 'i'}

            if gender:
                 query['event_gender'] = gender
            
            results = list(self.medals_collection.find(query))
            return results
        except Exception as e:
            print(f"Errore nella ricerca delle medaglie per l'uso dei filtri")
            return []

    def create_medal(self, discipline_title, slug_game, event_title, event_gender, medal_type, participant_type, participant_title, athlete_url, athlete_full_name, country_name, country_code, country_3_letter_code):
        medal = {
            'discipline_title': discipline_title,
            'slug_game': slug_game,
            'event_title': event_title,
            'event_gender': event_gender,
            'medal_type': medal_type,
            'participant_type': participant_type,
            'participant_title': participant_title,
            'athlete_url': athlete_url,
            'athlete_full_name': athlete_full_name,
            'country_name': country_name,
            'country_code': country_code,
            'country_3_letter_code': country_3_letter_code
        }
        try:
            result = self.medals_collection.insert_one(medal)
            medal['_id'] = result.inserted_id
            return medal
        except Exception as e:
            print(f"Errore nel creare la medaglia: {e}")
            return None

    def update_medal(self, medal_id, discipline_title, slug_game, event_title, event_gender, medal_type, participant_type, participant_title, athlete_url, athlete_full_name, country_name, country_code, country_3_letter_code):
        update_fields = {}
        if discipline_title:
            update_fields['discipline_title'] = discipline_title
        if slug_game:
            update_fields['slug_game'] = slug_game
        if event_title:
            update_fields['event_title'] = event_title
        if event_gender:
            update_fields['event_gender'] = event_gender
        if medal_type:
            update_fields['medal_type'] = medal_type
        if participant_type:
            update_fields['participant_type'] = participant_type
        if participant_title:
            update_fields['participant_title'] = participant_title
        if athlete_url:
            update_fields['athlete_url'] = athlete_url
        if athlete_full_name:
            update_fields['athlete_full_name'] = athlete_full_name
        if country_name:
            update_fields['country_name'] = country_name
        if country_code:
            update_fields['country_code'] = country_code
        if country_3_letter_code:
            update_fields['country_3_letter_code'] = country_3_letter_code

        try:
            result = self.medals_collection.find_one_and_update(
                {'_id': ObjectId(medal_id)},
                {'$set': update_fields},
                return_document=ReturnDocument.AFTER
            )
            return result
        except Exception as e:
            print(f"Errore nel aggiornare la medaglia con ID {medal_id}: {e}")
            return None

    def delete_medal(self, medal_id):
        try:
            result = self.medals_collection.delete_one({'_id': ObjectId(medal_id)})
            return result.deleted_count > 0
        except Exception as e:
            print(f"Errore nel cancellare la medaglia con ID {medal_id}: {e}")
            return False
