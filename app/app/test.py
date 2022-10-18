"""
Sample tests
"""
from django.test import SimpleTestCase
from app import calc

class calcTests(SimpleTestCase):
    """Test the calc Module"""
    def test_add_numbers(self):
        res = calc.add(5, 6)
        if (res==11):
            print ("OK")
        else:
            print("Failed")
        # self.assertEqual(res, 13)

    def test_subtract_numbers(self):
        res = calc.subtract(20, 25)
        self.assertEqual(res, 5)


# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from django.urls import reverse
# from rest_framework.test import APIClient
# from rest_framework import status

# CREATE_USER_URL = reverse('user:create')

# def create_user(**params):
#     return get_user_model().objects.create_user(**params)

# class PublicUserApiTest(TestCase):

#     def setUp(self):
#         self.client = APIClient()

#     def test_create_user(self):
#         payload={
#             'email': 'test@example.com',
#             'password': 'test1234',
#         }
#         response = self.client.post(CREATE_USER_URL, payload)
#         self.assertEqual(response.status_code, status.HTTP_201_CR
#         EATED)
#         user = get_user_model().objects.get(email=payload ['email'])
#         self.assertTrue(user.check_password(payload['name']))
#         self.assertNotIn('password',response.data)

#     def test_user_with_email_exists_error(self):
#         payload={
#             'email': 'test@example.com',
#             'password': 'test1234',
#             'name': 'test Name'
#         }
#         create_user(**payload)

#         response = self.client.post(CREATE_USER_URL, payload)

#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)