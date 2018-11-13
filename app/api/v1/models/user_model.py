from flask import make_response, jsonify, request
from flask_restful import reqparse


users = [
    {
        "user_id" : 43,
        "username" : "Alvin",
        "email": "Alvin@gmail.com",
        "default_location":"Kiambu",
        "password":"1234"
    },
    {
        "user_id" : 23,
        "username" : "Charity",
        "email": "Charity@gmail.com",
        "default_location":"Kericho",
        "password":"54321"
    },
    {
        "user_id" : 23,
        "username" : "Bilha",
        "email": "Bilha@gmail.com",
        "default_location":"Ngong",
        "password":"54321"
    }]

# User roles
customer = "Normal user"
admin = "User administrator"

class Users(object):
    """Creating model for users"""
    def __init__(self):
        self.udb = users
        self.user_id = len(self.udb)
        self.role = customer

    def create_user(self, username, email, default_location, password):
        user = {
            "user_id" :self.user_id + 1,
            "username": username,
            "email": email,
            "default_location": default_location,
            "password": password  
        } 

        save_user = self.udb.append(user)
        return save_user

    def filter_user_detail(self,email):
        user = [user for user in users if user['email']==email]
        return user

    def filter_password_detail(self,password):
        passw = [passw for passw in users if passw['password']==password]
        return passw

    def user_login(self, email, password):
        registered_user = Users.filter_user_detail(self, email)
        registered_user2 = Users.filter_password_detail(self, password)
        if not registered_user:
            return make_response(jsonify({
                "message" : "{} is not a registered user".format(email)
            }), 201)
        if registered_user:
            return make_response(jsonify({
                "message" : "login successful"
            }), 201)
        if not registered_user2:
            return make_response(jsonify({
                "message" : "{} is not a registered user".format(email)
            }), 400)
        elif registered_user2:
            return make_response(jsonify({
                "welcome" : "Login successful"
            }))