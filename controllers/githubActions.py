import env
from modules import *
import git
repo_dir=env.GITHUB_DIRECTORY
g = git.cmd.Git(repo_dir)


class pullGitHandler(tornado.web.RequestHandler):
    def get(self):
        proc = g.pull()
        message = {
            'tags': [
                'github',
                'pull',
            ],
            'status': 200,
            'message': proc,
            'repository_directory': repo_dir,
            'suggestions': ['Show me recent commits',
                            'Are there any updates on Github?']

        }
        self.write(message)


class repoStatusHandler(tornado.web.RequestHandler):
    def get(self):
        proc = g.status()
        message = {
            'tags': [
                'github',
                'status',
            ],
            'status': 200,
            'message': proc,
            'repository_directory': repo_dir,
            'suggestions': ['Show me recent commits']

        }
        self.write(message)

class repoLogsHandler(tornado.web.RequestHandler):
    def get(self):
        proc = g.log()
        message = {
            'tags': [
                'github',
                'logs',
            ],
            'status': 200,
            'message': proc,
            'repository_directory': repo_dir,
            'suggestions': ['Update code on the server',
                            'Are there any updates on Github?']

        }
        self.write(message)

