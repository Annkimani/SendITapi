import unittest
import json
from app.api.tests.test_base import BaseTest


class TestUser(BaseTest):
	def test_create_user(self):
		respo= self.client.post('/api/v1/users/signup',data = json.dumps(self.user_dummy_data),
								content_type='application/json')
		self.assertEqual(respo.status_code,201)


if __name__ == "__main__":
	unittest.main()

