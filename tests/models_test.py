import os
import sys
app_path = os.getcwd()
sys.path.insert(0,app_path)
testing = "%s/tmp/tests/log/application.log" % app_path
from nose.tools import eq_
import unittest
from log import Log
from mongodb import test_mongo

class TestUserModel(unittest.TestCase):

	def setUp(self):
		from models.users import Users
		self.model = Users()
		self.model.collection = test_mongo.get_collection('users')

	def test_create_user(self):
		self.model.collection.remove()
		self.model.create_user("test@test.com","password")
		eq_(1,self.model.collection.count())

	def test_check_user(self):
		self.model.collection.remove()
		self.model.create_user("test@test.com","password")
		assert {} != self.model.check_user("test@test.com", "password")

	def test_count_users(self):
		self.model.collection.remove()
		self.model.create_user("one@count.com","one")
		self.model.create_user("two@count.com","two")
		eq_(2,self.model.count_users())

	def test_existence(self):
		self.model.collection.remove()
		self.model.create_user("one@count.com","one")
		self.model.create_user("two@count.com","two")
		eq_(1,self.model.user_exists("two@count.com"))