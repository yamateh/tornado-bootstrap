import os
import sys

app_path = os.getcwd()
sys.path.insert(0,app_path)
testing = "%s/tmp/tests/log/application.log" % app_path
from nose.tools import eq_
import unittest
from log import Log
from mongodb import test_mongo


class TestLogging(unittest.TestCase):

    def test_log_db(self):
        Log.create('DB','',True)
        logs = test_mongo.get_collection('logs')
        logs.remove()
        Log.info('wololoo')
        eq_(1, logs.count())

    def test_log_file(self):

        if os.path.isfile(testing) :
            os.remove(testing)
        Log.create('FILE',testing,True)
        Log.info('wololo')
        eq_(True, os.path.isfile(testing))

    def test_log_type(self):
        Log.create('DB','',True)
        logs = test_mongo.get_collection('logs')
        logs.remove()
        Log.error('Traktorz')
        eq_("error",logs.find()[0]["type"])

    def test_log_message(self):
        Log.create('DB','',True)
        logs = test_mongo.get_collection('logs')
        logs.remove()
        Log.info('MyTur')
        eq_('MyTur',logs.find()[0]["message"])
