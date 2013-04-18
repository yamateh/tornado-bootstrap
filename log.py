import datetime
import logging
import os

class Log():
    instance = None

    DEST_FILE = 'FILE'
    DEST_DB = 'DB'

    #init logger based on file directory to store or on database
    def __init__(self, type='', log_file='', test=False):
        if type == self.DEST_FILE and log_file != '':
            log_file = os.path.abspath(log_file)
            #make sure we have a log directory
            dirname, filename = os.path.split(log_file)
            if not os.path.exists(dirname):
                os.makedirs(dirname)

            self._destination = self.DEST_FILE
            self._file_logger = logging.getLogger(__name__)
            hdlr = logging.FileHandler(log_file)
            hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(user)s %(message)s %(extended_info)s'))
            self._file_logger.addHandler(hdlr)
            self._file_logger.setLevel(logging.DEBUG)
        else:
            if not test :
                from mongodb import mongo
                self._db_logger = mongo.get_collection('logs') 
            else :
                from mongodb import test_mongo
                self._db_logger = test_mongo.get_collection('logs')
            self._destination = 'DB'

    # log message structure
    def message(self, type, message, user='', extended_info=''):
        if self._destination == 'DB':
            log_data = {
                'created':datetime.datetime.utcnow(),
                'message':message,
                'type':type,
                'user':user,
                'extended_info':extended_info
            }
            self._db_logger.insert(log_data)
        else:
            if type == 'access':
                type = 'info'

            getattr(self._file_logger, type)(message, extra={'user':user,'extended_info':extended_info})

    # creates new logger
    @staticmethod
    def create(type='FILE', log_file='', test=False):
        Log.instance = Log(type, log_file, test)

    '''
        Logging methods
    '''

    @staticmethod
    def access(message, user, extended_info):
        Log.instance.message('access', message, user, extended_info)

    @staticmethod
    def info(message, user=''):
        Log.instance.message('info', message, user)

    @staticmethod
    def debug(message, user=''):
        Log.instance.message('debug', message, user)

    @staticmethod
    def error(message, user=''):
        Log.instance.message('error', message, user)

    @staticmethod
    def warning(message, user=''):
        Log.instance.message('warning', message, user)

    @staticmethod
    def critical(message, user=''):
        Log.instance.message('critical', message, user)
