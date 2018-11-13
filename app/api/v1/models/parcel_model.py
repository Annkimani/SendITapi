from flask import make_response, jsonify, request
from flask_restful import reqparse

parcels = [
    {
        "order_id" : 1,
        "current_location": "Nairobi",
	    "receiver_name": "Anne",
	    "receivers_location": "kisumu",
	    "pickup_location": "delta",
	    "weight": 20,
	    "price": 1200,
	    "status": "pending"
    }]

# Order status after pickup
pending= "Your order is waiting to be sent"
on_transit= "in Transit"
delivered= "Delivered"
cancelled= "Cancelled"


class ParcelOrder(object):
    """Creating model for parcels"""
    def __init__(self):
        self.db = parcels
        self.order_id = len(self.db)
        self.status = pending

    def new_parcel(self, current_location,receiver_name ,receivers_location, pickup_location, weight, price):
        new_order_data = {
            "order_id": self.order_id + 1,
            "current_location": current_location,
            "receiver_name":receiver_name,
            "receivers_location":receivers_location,
            "pickup_location": pickup_location,
            "weight": weight,
            "price": price,
            "status": self.status
        }

        order = self.db.append(new_order_data)
        return order

    def parcels_list(self):
        return self.db

    def single_parcel(self, order_id):
        for parcel in parcels:
            if parcel["order_id"]== order_id:
                return parcel
            else:
                return {"parcel": "does not exist"}, 404
    
    def cancel_order(self, order_id):
        for parcel in parcels:
            if parcel["status"] == delivered:
                return {'parcel': "This parcel was already delivered and therefore cannot be canceled"}
            elif parcel['order_id'] == order_id:
                parcel.update({"status": cancelled})
                return {'parcel': 'Order Cancelled'}

    def clear(self):
    	self.db = []

    def get_orders_by_specific_user(self,user_id):
        """"Return orders by specific user"""
        user_orders = []
        for parcel in parcels:#Iterate over a sequence
            if (parcel['user_id'] == str(user_id)):
                user_orders.append(parcel)
            return user_orders
        return "Orders not found", 404
