from flask import Flask
import os

app = Flask(__name__)

# Settings
app.config.from_object('mycq.settings')
if 'MYCQ_SETTINGS' in os.environ:
    app.config.from_envvar('MYCQ_SETTINGS')


__import__('mycq.views')
