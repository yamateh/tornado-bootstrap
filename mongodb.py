try:
    import pymongo
except ImportError:
    pymongo = None

import exceptions
from config import settings

# pymongo wrapper
class Mongo():

    host = settings.MONGO['host']
    port = settings.MONGO['port']
    user = settings.MONGO['user']
    password = settings.MONGO['password']
    database = settings.MONGO['database']


    def __init__(self, dbsettings=None):
        if not pymongo:
            raise exceptions.ImproperlyConfigured(
                    "You need to install the pymongo library to use the "
                    "MongoDB backend.")
        if dbsettings != None:
            self.host = dbsettings['host']
            self.port = dbsettings['port']
            self.user = dbsettings['user']
            self.password = dbsettings['password']
            self.database = dbsettings['database']
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
        
        collection = db[collection]

        return collection

    def store_entry(self, entry, collection):
        """ Stores a system entry  """
        
        collection = self.get_collection(collection)
        
        if collection:
            collection.save(entry, safe=True)


        
mongo = Mongo()
test_mongo = Mongo(settings.TEST_MONGO)