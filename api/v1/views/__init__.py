#!/usr/bin/python3
""" init """
from flask import Blueprint
from api.v1.views.index import *
app_views = Blueprint('app_views', __name__)


@app_views.route('/api/v1')
