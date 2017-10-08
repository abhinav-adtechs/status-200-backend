'''
Preset controller by torn for / route
'''
from modules import *
import env

class homeHandler(tornado.web.RequestHandler):
    def get(self):
        ob = {
            'status': 'OK',
            'reponse': 'Application running',
            'token' : env.DO_ACCESS_TOKEN
        }
        self.write(tornado.escape.json_encode(ob))
