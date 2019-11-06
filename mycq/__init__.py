from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
application = app  # For Nginx Unit

# Settings
app.config.from_object('mycq.settings')
if 'MYCQ_SETTINGS' in os.environ:
    app.config.from_envvar('MYCQ_SETTINGS')

# User store
user_store = Redis(host=app.config['REDIS_HOST'],
                   port=app.config['REDIS_PORT'],
                   db=app.config['REDIS_USERS_DB'])

__import__('mycq.views')
