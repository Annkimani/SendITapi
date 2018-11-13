from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, reqparse
from app.api.v1.models.parcel_model import ParcelOrder, parcels

parcel = ParcelOrder()

class CreateParcels(Resource):
    def __init__(self):
       pass
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
    """Get the parcel details"""
    def get(self):
        return parcel.db
            
class SpecificOrder(Resource):
    """Get the specific parcel order using order_id"""
    def __init__(self):
        pass

    def get(self, order_id):
        data = request.get_json()
        single_order = parcel.single_parcel(order_id)
        return single_order

class CancelOrder(Resource):
    def __init__(self):
        """Cancelling the order"""
        pass
    def put(self, order_id):
        can_order = parcel.cancel_order(order_id)
        return can_order  
class GetOneOrder(Resource):
    def __init__(self):
        pass
    def get(self, order_id):
        """Getting the specific order using order ID"""
        all_user_orders = parcel.get_orders_by_specific_user(user_id)
        return all_user_orders