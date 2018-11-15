from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, reqparse
from app.api.v1.models import Users, users
from app.api.v1.models import ParcelOrder, parcels


required = reqparse.RequestParser()
required.add_argument('email', help = "Fill the email details", required = True)
required.add_argument('password', help = "Fill the password", required = True)

user_save = Users()
parcel = ParcelOrder()

class UserSignup(Resource):
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

class CreateParcels(Resource):
    def post(self):
        data = request.get_json()
        current_location = data['current_location']
        receiver_name = data['receiver_name']
        receivers_location = data['receivers_location']
        pickup_location = data['pickup_location']
        weight = data['weight']
        price = data['price']
        parcel.new_parcel(current_location, receiver_name, receivers_location, pickup_location,weight,price)
        parcel = parcel.db
        return make_response(jsonify({"message": "The parcel order has been successfully created"}), 200)

class AllOrders(Resource):
    def get(self):
        return parcel.db
            
class SpecificOrder(Resource):

    def get(self, order_id):
        # data = request.get_json()
        single_order = parcel.single_parcel(order_id)
        return single_order

class CancelOrder(Resource):
    def put(self, order_id):
        can_order = parcel.cancel_order(order_id)
        return can_order 

class GetOneOrder(Resource):
    def get(self, username):
        all_user_orders = parcel.get_orders_by_specific_user(username)
        return all_user_orders

        