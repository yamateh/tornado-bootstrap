try:
    import pymongo
except ImportError:
    pymongo = None

import exceptions
from config import settings

# pymongo wrapper
class Mongo():

    # Cron is for testing purposes
    internal_collections = ['logs','sessions']
    application_collections = []

    host = settings.MONGO['host']
    port = settings.MONGO['port']
    user = settings.MONGO['user']
    password = settings.MONGO['password']
    database = settings.MONGO['database']
    valid_collections = internal_collections \
                        + application_collections

    def __init__(self):
        if not pymongo:
            raise exceptions.ImproperlyConfigured(
                    "You need to install the pymongo library to use the "
                    "MongoDB backend.")

        self._database = None
        self._connection = None
    
    def get_connection(self):
        """Connect to the MongoDB server."""
        from pymongo.connection import Connection
        
        if self._connection is None:
            self._connection = Connection(self.host, self.port)
            return self._connection
    
    def get_database(self):
        """"Get database from MongoDB connection. """
        if self._database is None:
            conn = self.get_connection()
            db = conn[self.database]
            self._database = db

        return self._database

    def get_collection(self, collection):
        db = self.get_database()
        
        if collection in self.valid_collections:            
            collection = db[collection]
        else:
            return False

        return collection

    def store_entry(self, entry, collection):
        """ Stores a system entry  """
        
        collection = self.get_collection(collection)
        
        if collection:
            collection.save(entry, safe=True)


        
mongo = Mongo()