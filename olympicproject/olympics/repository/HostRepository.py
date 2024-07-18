from pymongo import MongoClient, ReturnDocument
from bson.objectid import ObjectId

from datetime import datetime
from dateutil import parser
from bson import ObjectId

class HostRepository:
    def __init__(self, db_url, db_name):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.hosts_collection = self.db['hosts']

    def get_all_hosts(self):
        try:
            return list(self.hosts_collection.find())
        except Exception as e:
            print(f"Errore nel recuperare tutti gli host: {e}")
            return []

    def get_host_by_id(self, host_id):
        try:
            host = self.hosts_collection.find_one({'_id': ObjectId(host_id)})
            if host:
                host['game_end_date'] = self.format_date(host.get('game_end_date'))
                host['game_start_date'] = self.format_date(host.get('game_start_date'))
            return host
        except Exception as e:
            print(f"Errore nel recuperare l'host con ID {host_id}: {e}")
            return None

    @staticmethod
    def format_date(date_str):
        if date_str:
            try:
                date_obj = parser.isoparse(date_str) if isinstance(date_str, str) else date_str
                return date_obj.date().isoformat()
            except Exception as e:
                print(f"Errore nella conversione della data: {e}")
                return date_str
        return date_str
        
        

    def search_hosts(self, search_query, season):
        try:
            # Utilizziamo il regex per cercare la stringa parziale in tutti i campi
            # Base query
            query = {
                '$and':[
                    {
                        '$or': [
                            {'game_slug': {'$regex': search_query, '$options': 'i'}},
                            {'game_name': {'$regex': search_query, '$options': 'i'}},
                        ]
                    },
                    {'game_season': {'$regex': season, '$options': 'i'}}
                ]
                
            }

            #if season:
            #    query['$and'] = [{'game_season': {'$regex': season, '$options': 'i'}}]
                    #
                    #{'game_end_date': {'$regex': search_query, '$options': 'i'}},
                    #{'game_start_date': {'$regex': search_query, '$options': 'i'}},
                    #{'game_location': {'$regex': search_query, '$options': 'i'}},
                    #{'game_year': {'$regex': search_query, '$options': 'i'}}
            results = list(self.hosts_collection.find(query))
            return results
        except Exception as e:
            print(f"Errore nella ricerca degli host per '{search_query}': {e}")
            return []
        
    def filter_by_season(self, search_query):
        try:
            # Utilizziamo il regex per cercare la stringa parziale in tutti i campi
            query = {
                '$or': [
                    {'game_slug': {'$regex': search_query, '$options': 'i'}},
                    {'game_end_date': {'$regex': search_query, '$options': 'i'}},
                    {'game_start_date': {'$regex': search_query, '$options': 'i'}},
                    {'game_location': {'$regex': search_query, '$options': 'i'}},
                    {'game_name': {'$regex': search_query, '$options': 'i'}},
                    {'game_season': {'$regex': search_query, '$options': 'i'}},
                    {'game_year': {'$regex': search_query, '$options': 'i'}}
                ]
            }
            results = list(self.hosts_collection.find(query))
            return results
        except Exception as e:
            print(f"Errore nella ricerca degli host per '{search_query}': {e}")
            return []


    def create_host(self, game_end_date, game_start_date, game_location, game_name, game_season, game_year):
        # Ricava game_slug da game_name e rendilo tutto minuscolo
        game_slug = '-'.join(game_name.split()).lower()

        host = {
            'game_slug': game_slug,
            'game_end_date': game_end_date,
            'game_start_date': game_start_date,
            'game_location': game_location,
            'game_name': game_name,
            'game_season': game_season,
            'game_year': game_year
        }
        try:
            result = self.hosts_collection.insert_one(host)
            host['_id'] = result.inserted_id
            return host
        except Exception as e:
            print(f"Errore nel creare l'host: {e}")
            return None

    def update_host(self, host_id, game_end_date=None, game_start_date=None, game_location=None, game_name=None, game_season=None, game_year=None):
        update_fields = {}

        if game_name:
            game_slug = '-'.join(game_name.split()).lower()  # Ricava e rendi game_slug tutto minuscolo da game_name
            update_fields['game_slug'] = game_slug
        
        if game_end_date:
            update_fields['game_end_date'] = game_end_date
        if game_start_date:
            update_fields['game_start_date'] = game_start_date
        if game_location:
            update_fields['game_location'] = game_location
        if game_name:
            update_fields['game_name'] = game_name
        if game_season:
            update_fields['game_season'] = game_season
        if game_year:
            update_fields['game_year'] = game_year

        try:
            result = self.hosts_collection.find_one_and_update(
                {'_id': ObjectId(host_id)},
                {'$set': update_fields},
                return_document=ReturnDocument.AFTER
            )
            return result
        except Exception as e:
            print(f"Errore nel aggiornare l'host con ID {host_id}: {e}")
            return None
    def delete_host(self, host_id):
        try:
            result = self.hosts_collection.delete_one({'_id': ObjectId(host_id)})
            return result.deleted_count > 0
        except Exception as e:
            print(f"Errore nel cancellare l'host con ID {host_id}: {e}")
            return False
