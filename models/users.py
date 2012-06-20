import datetime
import hashlib, hmac, base64, re
from mongodb import mongo


class Users(object):

    def __init__(self):
        super(Users, self).__init__()
        self.collection = mongo.get_collection('users')

    def create_user(self, email, password):
        user_schema = {
            "email": email,
            "password": hashlib.sha1(password.encode('utf-8')).hexdigest(),
            "created_at": datetime.datetime.utcnow()
        }
        self.collection.save(user_schema)

    def check_user(self, email, password):
        passw = hashlib.sha1(password.encode('utf-8')).hexdigest()
        result = self.collection.find_one({"email": email,
                                    "password": passw})

        return result if result else {}

    
    def count_users(self):
         return self.collection.count() 

    def user_exists(self, email):
        result = self.collection.find({"email": email}).count()
        return result

users = Users()