#!/usr/bin/python3
"""view for User objects that handles all default RESTFul API actions"""
from flask import jsonify
from flask import abort
from flask import request
from models.user import User
from models import storage
from api.v1.views import app_views


@app_views.route('/user', methods=['GET'])
def user():
    """Retrieves the list of all User objects"""
    try:
        Users = storage.all(User)
        UserList = []
        for k in Users:
            UserList.append(Users[k].to_dict())
        return jsonify(UserList)
    except:
        abort(404)


@app_views.route("/user/<string:user_id>", methods=['GET'])
def getMethod(user_id):
    """Retrieves a User object"""
    try:
        user = storage.get(User, user_id).to_dict()
        return jsonify(user)
    except:
        abort(404)


@app_views.route("/user/<user_id>", methods=['DELETE'])
def deleteMethod(user_id):
    """Deletes a User object"""
    try:
        storage.delete(User, user_id)
        storage.save()
        return {}, 200
    except:
        abort(404)


@app_views.route("/user", methods=['POST'], endpoint='userPost')
def postMethod():
    """Creates a User"""
    data = request.get_json()
    if not data:
        abort(400, "Not a JSON")
    if 'email' not in data:
        abort(400, "Missing email")
    if 'password' not in data:
        abort(400, "Missing password")
    instance = User(**data)
    instance.save()
    return jsonify(instance.to_dict()), 201


@app_views.route("/user/<user_id>", methods=['PUT'])
def putMethod(user_id):
    """Updates a User object"""
    k = "User." + str(user_id)
    if k not in storage.all():
        abort(404)
    data = request.get_json()
    if not request.is_json:
        abort(400, "Not a JSON")
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at', 'email']:
            setattr(storage.all()[k], key, value)
    storage.all()[k].save()
    return jsonify(storage.get(User, user_id).to_dict()), 200
