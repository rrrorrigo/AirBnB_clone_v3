#!/usr/bin/python3
""" init """
from flask import Blueprint
from models.engine.db_storage import DBStorage


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *

storage = DBStorage
storage.reload()
