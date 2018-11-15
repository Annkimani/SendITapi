import unittest
import json
from app.api.tests.test_base import BaseTest


class TestUser(BaseTest):
	def test_user_login(self):
		respo= self.client.post('/api/v1/users/login',data = json.dumps(self.login_dummy_data),
								content_type='application/json')
		self.assertEqual(respo.status_code,201)


if __name__ == "__main__":
	unittest.main()

