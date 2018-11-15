import unittest
import sys  # fix import errors
from app import create_app
import os
from app.api.v1.models import ParcelOrder, Users

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

parcels = ParcelOrder()
user = Users()


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.parcel_dummy_data = {
        "parcel_id" : 1,
	    "receiver_name": "Anne",
	    "receivers_location": "kisumu",
	    "pickup_location": "delta",
	    "weight": 20,
	    "price": 1200,
	    "status": "pending"
    }

        self.user_dummy_data = {
            "user_id": 1,
            "username": "Hannah",
            "email": "hannah@gmail.com",
            "default_location": "nairobi",
            "password": 0000
        }
        self.login_dummy_data = {
            "email": "hannnah@gmail.com",
            "password": 1234
        }

    def tearDown(self):
        parcels.db.clear()


        