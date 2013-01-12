import textwrap

import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.web

from tornado.options import define, options
define('port', default=8000, type=int)

class ReverseHandler(tornado.web.RequestHandler):
    def get(self, _input):
        self.write(_input[::-1])
        
class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        txt = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(txt, width))
        
if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers = [
            (r'/reverse/(\w+)', ReverseHandler),
            (r'/wrap', WrapHandler)
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()