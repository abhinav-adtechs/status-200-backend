'''
Preset controller by torn for / route
'''
import digitalocean
import json
import env
from modules import *


class listDropletsHandler(tornado.web.RequestHandler):
    def get(self):
        manager = digitalocean.Manager(token=env.DO_ACCESS_TOKEN)
        my_droplets = manager.get_all_droplets()
        droplet_info = []
        droplet_names = []
        droplet_size = []
        droplet_server_status = []
        for droplet in my_droplets:
            droplet_info.append({
                'name': droplet.name,
                'size': droplet.size_slug,
                'server_status': droplet.status
            })
            droplet_names.append(droplet.name)
            droplet_server_status.append(droplet.status)
            droplet_size.append(droplet.size_slug)

        droplet_names_string = ', '.join([str(x) for x in droplet_names])
        droplet_size_string = ', '.join([str(x) for x in droplet_size])
        message = "You have " + str(len(droplet_size)) + ' droplets in your account named ' + droplet_names_string
        message = message + " of size " + droplet_size_string + ". Servers are up and healthy playing in your account"
        ob = {
            'status': 'OK',
            'tags': [
                'do',
                'list',
                'droplet'
            ],
            'details': droplet_info,
            'message': message,
            'suggestions': ['Create a new server']


        }
        self.write(ob)


class createDropletHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument('name', 'HackInOutSample')
        region = 'blr1'
        image = 'ubuntu-16-04-x64'
        size = '512mb'
        droplet = digitalocean.Droplet(token=env.DO_ACCESS_TOKEN,
                                       name=name,
                                       region=region,  # New York 2
                                       image=image,  # Ubuntu 14.04 x64
                                       size_slug=size,  # 512MB
                                       backups=True)
        droplet.create()
        message = {
            'status': 200,
            'tags': [
                'do',
                'create',
                'droplet'
            ],
            'message': 'Voila! Your server named ' + name + ' has been created successfully! Please check your email for further details! Happy Coding!',
            'specifications': {
                'size': size,
                'region': region,
                'image': image,
            },
            'suggestions': ['List me all the servers']
        }
        self.write(message)

class accountDetailHandler(tornado.web.RequestHandler):
    def get(self):
        manager = digitalocean.Manager(token=env.DO_ACCESS_TOKEN)
        account = manager.get_account()
        details = {
            'tags': [
                'do',
                'account',
                'details'
            ],
            'account_status': account.status,
            'emial_verified': account.email_verified,
            'droplet_limit': account.droplet_limit,
            'registered_email': account.email,
            'message': 'Your account email address is ' + str(account.email) + ' and the droplet limit is ' + str(account.droplet_limit) + '. Your account is ' + (account.status)+' . May the force be with you!',
            'suggestions': ['Create a new server',
                            'List all the servers']
        }
        self.write(details)

