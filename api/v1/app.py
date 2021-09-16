#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)

@app.teardown_appcontext
def close():
    """display on route / Hello HBNB!"""
    storage.close()

if __name__ == '__main__':
    hostHBNB = getenv('HBNB_API_HOST')
    portHBNB = getenv('HBNB_API_PORT')
    host = hostHBNB if hostHBNB else '0.0.0.0'
    port = portHBNB if portHBNB else '5000'
    app.run(host=host, port=port, threaded=True)
