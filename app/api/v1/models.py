from flask import make_response, jsonify, request
from flask_restful import reqparse


users = [
    {
        "user_id" : 2,
        "username" : "Hannah",
        "email": "hannah@gmail.com",
        "password":"0000"
    }]


parcels = [
    {
        "parcel_id" : 1,
        "sender_location": "Nairobi",
	    "receiver_name": "Anne",
	    "pickup_location": "delta",
	    "weight": 20,
	    "price": 1200,
	    "status": "pending"
    }]

pending= "Your order is waiting to be sent"
on_transit= "in Transit"
delivered= "Delivered"
cancelled= "Cancelled"

class Users(object):
    def __init__(self):
        self.udb = users
        self.user_id = len(self.udb)

    def create_user(self, username, email, password):
        user = {
            "user_id" :self.user_id + 1,
            "username": username,
            "email": email,
            "password": password  
        } 

        save_user = self.udb.append(user)
        return save_user

    def filter_user_detail(self,email):
        user = [user for user in users if user['email']==email]
        return user

    def filter_password_detail(self,password):
        psswrd = [psswrd for psswrd in users if psswrd['password']==password]
        return psswrd

    def user_login(self, email, password):
        user_A = Users.filter_user_detail(self, email)
        user_B = Users.filter_password_detail(self, password)
        if not user_A:
            return make_response(jsonify({
                "message" : "{} is not a registered user".format(email)
            }), 201)
        if user_A:
            return make_response(jsonify({
                "message" : "login successful"
            }), 201)
        if not user_B:
            return make_response(jsonify({
                "message" : "{} is not a registered user".format(email)
            }), 400)
        elif user_B:
            return make_response(jsonify({
                "welcome" : "Login successful"
            }))

class ParcelOrder(object):
    def __init__(self):
        self.db = parcels
        self.parcel_id = len(self.db)
        self.status = pending

    def new_parcel(self, sender_location,receiver_name ,receiver_location, pickup_location, weight, price):
        new_order_data = {
            "parcel_id": self.parcel_id + 1,
            "sender_location": sender_location,
            "receiver_name":receiver_name,
            "pickup_location": pickup_location,
            "weight": weight,
            "price": price,
            "status": self.status
        }

        order = self.db.append(new_order_data)
        return order

    def parcels_list(self):
        return self.db

    def single_parcel(self, parcel_id):
        for parcel in parcels:
            if parcel["parcel_id"]== parcel_id:
                return parcel
            else:
                return {"parcel": "does not exist"}, 404
    
    def cancel_order(self, parcel_id):
        for parcel in parcels:
            if parcel["status"] == delivered:
                return {'parcel': "Failed. Parcel already delivered"}
            elif parcel['parcel_id'] == parcel_id:
                parcel.update({"status": cancelled})
                return {'parcel': 'Order Cancelled'}

    def clear(self):
    	self.db = []

    def get_orders_by_specific_user(self,user_id):
        user_orders = []
        for parcel in parcels:
            if (parcel['user_id'] == user_id):
                user_orders.append(parcel)
            return user_orders
        return "Orders not found", 404

