#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
from flask import jsonify


app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views, url_prefix='/api/v1')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.teardown_appcontext
def bye(self):
    """display on route / Hello HBNB!"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """handler for 404 errors that returns a JSON-formatted 404 status code response"""
    return jsonify(error="Not found"), 404


@app.after_request
def after_request(response):
    """create a CORS instance allowing: /* for 0.0.0.0"""
    response.headers["Access-Control-Allow-Origin"] = "0.0.0.0"
    return response

if __name__ == '__main__':
    hostHBNB = getenv('HBNB_API_HOST')
    portHBNB = getenv('HBNB_API_PORT')
    host = hostHBNB if hostHBNB else '0.0.0.0'
    port = portHBNB if portHBNB else '5000'
    app.run(host=host, port=port, threaded=True)    
