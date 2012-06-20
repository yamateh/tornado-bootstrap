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

class Application():
    def __init__(self):
        self.application = None

    def init_routes(self):
        from routes import RouteLoader
        return RouteLoader.load('controllers')

    #Init logging on database or file
    def init_logging(self,log):
            if log == 'db':
                Log.create()
            else:
                Log.create('FILE',log)

    def main(self):

        #settings passed to tornado app
        tornado_settings = {
            "static_path": settings.static_path,
            "cookie_secret": settings.cookie_secret,
            "login_url": settings.login_url,
        }

        #init a logger
        self.init_logging(settings.log)

        #routes
        routes = self.init_routes()

        self.application = web.Application(routes,**tornado_settings)

        http_server = httpserver.HTTPServer(self.application)
        http_server.listen(settings.port)

        Log.info("Ready and listening")

        ioloop = tornado.ioloop.IOLoop().instance()
        autoreload.start(ioloop)
        try:
            ioloop.start()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    (Application()).main()