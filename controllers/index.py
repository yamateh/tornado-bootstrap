from tornado.web import RequestHandler
from routes import route

@route('/')
class IndexHandler(RequestHandler):
    def get(self):
        self.render('index.html')
