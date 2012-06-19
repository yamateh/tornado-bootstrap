import sys
import tornado.ioloop
from log import Log
from tornado import autoreload
from tornado import web
from tornado import httpserver
from config import settings

#Temp handler, this will be removed
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

#Init logging on database or file
def init_logging(log):
        if log == 'db':
            Log.create()
        else:
            Log.create('FILE',log)

def main():

    #settings passed to tornado app
    tornado_settings = {
        "static_path": settings.static_path,
        "cookie_secret": settings.cookie_secret,
        "login_url": settings.login_url,
    }

    #init a logger
    init_logging(settings.log)

    #routes
    #TODO: change to dynamic init from controllers
    routes = [(r"/", MainHandler)]

    application = web.Application(routes,**tornado_settings)

    http_server = httpserver.HTTPServer(application)
    http_server.listen(settings.port)

    Log.info("Ready and listening")

    ioloop = tornado.ioloop.IOLoop().instance()
    autoreload.start(ioloop)
    try:
        ioloop.start()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()