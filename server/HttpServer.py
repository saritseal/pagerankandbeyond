import cherrypy
import random

class Root(object):

    random_str = int(random.random() * 100)
    @cherrypy.expose
    def index(self):
        return "Hello World!" + str(self.random_str)

app = cherrypy.tree.mount(Root(), '/')

# if __name__ == '__main__':
#
#     cherrypy.engine.autoreload.unsubscribe()
#     cherrypy.engine.timeout_monitor.unsubscribe()
#
#     cherrypy.config.update({
#         '/': {
#             'server.thread_pool' : 20,
#             'tools.sessions.on': True,
#             'tools.gzip.on' : True,
#             'server.socket_host': '127.0.0.1',
#             'server.socket_port': 8080,
#         }
#     })
#
#     cherrypy.quickstart(Root())

