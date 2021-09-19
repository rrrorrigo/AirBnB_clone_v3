#!/usr/bin/python3
"""view for City objects that handles all default RESTFul API actions"""
from flask import jsonify
from flask import abort
from flask import request
from models.city import City
from models import storage
from api.v1.views import app_views


@app_views.route('/cities', methods=['GET'])
def cities():
    """Retrieves the list of all City objects"""
    try:
        cities = storage.all(City)
        CityList = []
        for k in cities:
            CityList.append(cities[k].to_dict())
        return jsonify(CityList)
    except:
        abort(404)


@app_views.route("/cities/<string:City_id>", methods=['GET'])
def getMethod(City_id):
    """Retrieves a City object"""
    try:
        cities = storage.get(City, City_id).to_dict()
        return jsonify(cities)
    except:
        abort(404)


@app_views.route("/cities/<City_id>", methods=['DELETE'])
def deleteMethod(City_id):
    """Deletes a City object"""
    try:
        storage.delete(City, City_id)
        storage.save()
        return {}, 200
    except:
        abort(404)


@app_views.route("/cities", methods=['POST'], endpoint='CitysPost')
def postMethod():
    """Creates a City"""
    data = request.get_json()
    if not data:
        abort(400, "Not a JSON")
    if 'name' not in data:
        abort(400, "Missing name")
    instance = City(**data)
    instance.save()
    return jsonify(instance.to_dict()), 201


@app_views.route("/cities/<City_id>", methods=['PUT'])
def putMethod(City_id):
    """Updates a City object"""
    k = "City." + str(City_id)
    if k not in storage.all():
        abort(404)
    data = request.get_json()
    if not request.is_json:
        abort(400, "Not a JSON")
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at', 'state_id']:
            setattr(storage.all()[k], key, value)
    storage.all()[k].save()
    return jsonify(storage.get(City, City_id).to_dict()), 200
