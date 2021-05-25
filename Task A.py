'''a)	As the first task you should use pet swagger: https://petstore.swagger.io/
Endpoint - users.
You need to write CRUD operation tests for testing this endpoint.'''

# class PetstoreUserTests (unittest.TestCase):

    # def Test_CreateUser(self):
    #     response = requests.post(
    #         'https://petstore.swagger.io/v2/user/createWithList',
    #         [
    #             {
    #                 "id": 0,
    #                 "username": "WBA",
    #                 "firstName": "Tom",
    #                 "lastName": "Cook",
    #                 "email": "string@gmail.com",
    #                 "password": "string",
    #                 "phone": "103",
    #                 "userStatus": 0
    #             },
    #         ]
    #     )
    #     self.assertEqual(response.status_code, 200)

    # def Test_GetUser(self):
    #     response = requests.get("https://petstore.swagger.io/v2/user/butcher")
    #     self.assertEqual(response.status_code, 200)
    #     print('Test GetUser completed')

    # def Test_UpdateUser(self):
    #     response = requests.put("https://petstore.swagger.io/v2/user/butcher",
    #                             {
    #                                 # "id": 0,
    #                                 "username": "butcher",
    #                                 "firstName": "vova",
    #                                 "lastName": "string",
    #                                 "email": "string@hoo",
    #                                 "password": "string",
    #                                 "phone": "string",
    #                                 "userStatus": 0
    #                             }
    #                             )
    #     self.assertEqual(response.status_code, 200)
    #     print('Test UpdateUser completed')

# if __name__ == '__main__':
#     unittest.main()

import requests
import json
import unittest

class TestPetStoreUser(unittest.TestCase):

    def payload_create(self):
        return {"id": "1", "username": "username", "firstName": "firstname", "lastName": "lastName", "email": "string",
  "password": "string",  "phone": "string"}

    # def payload_login(self):
    #     return {"id": "1", "username": "username", "password": "password"}

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

    # def test_login_user(self):
    #         resp = requests.get('https://petstore.swagger.io/v2/user/username', data=json.dumps(self.payload_create()),
    #                             headers=self.header())
    #         self.assertEqual(resp.status_code, 200)
    #
    # def test_logout_user(self):
    #     resp = requests.put('https://petstore.swagger.io/v2/user/logout', data=json.dumps(self.payload_login()),
    #                         headers=self.header())
    #     self.assertEqual(resp.status_code, 200)

    # def test_create_user_with_Array(self):

    # def test_create_user(self):

if __name__ == '__main__':
    unittest.main()