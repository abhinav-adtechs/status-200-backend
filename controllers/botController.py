import env
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from modules import *
import requests

CREATE_SERVER_MESSAGE = "create server named this"
LIST_SERVERS_MESSAGE = "list all servers"
LIST_CLOUD_DETAILS = "what is my cloud status"
GITHUB_PULL_COMMAND = "update code on server"
GITHUB_CODE_STATUS = "any new changes on github"
GITHUB_LOGS_MESSAGE = "show me recent commits"

class chatHandler(tornado.web.RequestHandler):
    def get(self):
        message = self.get_argument('message')
        fuzz_ratios = []
        fuzz_ratios.append(fuzz.ratio(message, CREATE_SERVER_MESSAGE))
        fuzz_ratios.append(fuzz.ratio(message, LIST_SERVERS_MESSAGE))
        fuzz_ratios.append(fuzz.ratio(message, LIST_CLOUD_DETAILS))
        fuzz_ratios.append(fuzz.ratio(message, GITHUB_PULL_COMMAND))
        fuzz_ratios.append(fuzz.ratio(message, GITHUB_CODE_STATUS))
        fuzz_ratios.append(fuzz.ratio(message, GITHUB_LOGS_MESSAGE))
        max_ratio = max(fuzz_ratios)
        for i in fuzz_ratios:
            if i==max_ratio:
                index=fuzz_ratios.index(i)
        if index==0:
            server_name="default"
            m = message.split(" ")
            for i in range(len(m)):
                if m[i].lower() == "named":
                    server_name = m[i+1]

            url = env.API_SERVER_URL+"api/do/droplet/create?name="+server_name
            r=requests.get(url)
            self.write(r.text)
        elif index==1:
            url = env.API_SERVER_URL+"api/do/droplets/list"
            r = requests.get(url)
            self.write(r.text)
        elif index==2:
            url = env.API_SERVER_URL+"api/do/details"
            r = requests.get(url)
            self.write(r.text)
        elif index==3:
            url = env.API_SERVER_URL+"api/github/pull"
            r = requests.get(url)
            self.write(r.text)
        elif index==4:
            url = env.API_SERVER_URL + "api/github/status"
            r = requests.get(url)
            self.write(r.text)
        elif index==5:
            url = env.API_SERVER_URL + "api/github/logs"
            r = requests.get(url)
            self.write(r.text)
        else:
            self.write({
                'status': 200,
                'message': 'I\'m so sorry but I couldn\'t get you.'
            })
