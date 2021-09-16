#!/usr/bin/python3
""" index """
from api.v1.views import app_views
import json
st = app_views(st)

st.route('/status')
def status():
    return json.dump({'status': 'OK'})
