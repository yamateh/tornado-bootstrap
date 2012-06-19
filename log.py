import pymongo, datetime, logging, os
from mongodb import mongo

class Log():
    instance = None
    
    #init logger based on file directory to store or on database
    def __init__(self,type='',log_file=''):
        if type == 'FILE' and log_file != '':
            #make sure we have a log directory
            dirname, filename = os.path.split(log_file)
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            
            self.destination = 'FILE'
            self.file_logger = logging.getLogger(__name__)
            hdlr = logging.FileHandler(log_file)
            hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(user)s %(message)s %(extended_info)s'))
            self.file_logger.addHandler(hdlr)
            self.file_logger.setLevel(logging.DEBUG)
        else:
            self.logs = mongo.get_collection('logs') 
            self.destination = 'DB'

    # log message structure
    def message(self, type, message, user='', extended_info=''):
        if self.destination == 'DB':    
            log_data = {
                'created':datetime.datetime.utcnow(),
                'message':message,
                'type':type,
                'user':user,
                'extended_info':extended_info
            }
            self.logs.insert(log_data)
        else:
            if type == 'access':
                type = 'info'
            
            getattr(self.file_logger, type)(message,extra={'user':user,'extended_info':extended_info})
    
    # creates new logger
    @staticmethod
    def create(type='FILE',log_file=''):
        Log.instance = Log(type,log_file)
        
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