'''a)	As the first task you should use pet swagger: https://petstore.swagger.io/
Endpoint - users.
You need to write CRUD operation tests for testing this endpoint.'''



import requests
import json
import unittest

class TestPetStoreUser(unittest.TestCase):

    def payload_create(self):
        return {
            "id": "1", "username": "username", "firstName": "firstname", "lastName": "lastName", "email": "string",
  "password": "string",  "phone": "string"
        }

    def payload_create_with_list(self):
        return [
            {
                "id": "1", "username": "username", "firstName": "firstname", "lastName": "lastName", "email": "string",
                "password": "string", "phone": "string"
            }
        ]

    def payload_login(self):
        return {"id": "1", "username": "username", "password": "password"}

    def header(self):
        return {'Content-Type': 'application/json'}

    def test_1_create_user(self):
        resp = requests.post('https://petstore.swagger.io/v2/user', data=json.dumps(self.payload_create()),
                             headers=self.header())
        self.assertEqual(resp.status_code, 200)
        print('test 1 completed')

    def test_2_read_user(self):
        resp = requests.get('https://petstore.swagger.io/v2/user/username')
        self.assertEqual(resp.status_code, 200)
        print('test 2 completed')

    def test_3_update_user(self):
        resp = requests.put('https://petstore.swagger.io/v2/user/username', data=json.dumps(self.payload_create()),
                            headers=self.header())
        self.assertEqual(resp.status_code, 200)
        print('test 3 completed')

    def test_4_delete_user(self):
        resp = requests.delete('https://petstore.swagger.io/v2/user/username')
        self.assertEqual(resp.status_code, 200)
        print('test 4 completed')

    def test_5_login_user(self):
        resp = requests.get('https://petstore.swagger.io/v2/user/login', data=json.dumps(self.payload_login()),
                            headers=self.header())
        self.assertEqual(resp.status_code, 200)
        print('test 5 completed')

    def test_6_logout_user(self):
        resp = requests.get('https://petstore.swagger.io/v2/user/logout')
        self.assertEqual(resp.status_code, 200)
        print('test 6 completed')


    def test_7_create_user_with_list(self):
        resp = requests.post('https://petstore.swagger.io/v2/user/createWithList', data=json.dumps(self.payload_create_with_list()),
                             headers=self.header())
        self.assertEqual(resp.status_code, 200)
        print('test 7 completed')

    def test_8_create_user_with_array(self):
        resp = requests.post('https://petstore.swagger.io/v2/user/createWithArray', data=json.dumps(self.payload_create_with_list()),
                             headers=self.header())
        self.assertEqual(resp.status_code, 200)
        print('test 8 completed')


if __name__ == '__main__':
    unittest.main()