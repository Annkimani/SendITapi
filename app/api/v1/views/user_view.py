from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, reqparse
from app.api.v1.models.user_model import Users, users

"""details for user login"""
required = reqparse.RequestParser()
required.add_argument('email', help = "Fill the email details", required = True)
required.add_argument('password', help = "Fill the password", required = True)

user_save = Users()

class UserSignup(Resource):
    """registering a new user"""
    def post(self):
        data = request.get_json()
        username = data["username"]
        email = data["email"]
        default_location = data["default_location"]
        password = data["password"]
        user_save.create_user(username, email, default_location, password)
        user_save = user_save.udb
      
        return make_response(jsonify({
            "message" : "User has been successfully created",
            
        }),201)


class UserLogin(Resource):
    def post(self):
        user = required.parse_args()
        return Users.user_login(self,user['email'], user['password'])

