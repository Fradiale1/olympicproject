from pymongo import MongoClient, ReturnDocument
from bson.objectid import ObjectId

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
            return self.hosts_collection.find_one({'_id': ObjectId(host_id)})
        except Exception as e:
            print(f"Errore nel recuperare l'host con ID {host_id}: {e}")
            return None

    def create_host(self, game_slug, game_end_date, game_start_date, game_location, game_name, game_season, game_year):
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

    def update_host(self, host_id, game_slug=None, game_end_date=None, game_start_date=None, game_location=None, game_name=None, game_season=None, game_year=None):
        update_fields = {}
        if game_slug:
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
