from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status


class AuthApiTestCase(TestCase):

    def setUp(self):
        """
        Подготавливаем данные для тестов.
        Будет выполняться перед входом в каждый из методов,
        начинающихся с `test_`.
        """
        self.username = 'test'
        self.password = 'pass1234'
        self.user = User.objects.create_user(
            first_name='Test',
            last_name='Testovich',
            username=self.username,
            password=self.password,
            email='test@example.com'
        )

    def test_auth_login_endpoint(self):
        credentials = {
            'username': self.username,
            'password': self.password,
        }
        url = reverse('auth-login')
        response = self.client.post(url, data=credentials,
                                    content_type='application/json')
        self.assertTrue(response.status_code, status.HTTP_200_OK)
        expected_response = {'details': 'You successfully logged in'}
        self.assertDictEqual(response.data, expected_response)

    def test_auth_login_endpoint_without_username(self):
        credentials = {
            'password': self.password,
        }
        url = reverse('auth-login')
        response = self.client.post(url, data=credentials,
                                    content_type='application/json')
        self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)

    def test_auth_login_endpoint_without_password(self):
        credentials = {
            'username': self.username,
        }
        url = reverse('auth-login')
        response = self.client.post(url, data=credentials,
                                    content_type='application/json')
        self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)

    def test_auth_login_endpoint_without_data(self):
        credentials = {}
        url = reverse('auth-login')
        response = self.client.post(url, data=credentials,
                                    content_type='application/json')
        self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)
        error_keys = list(response.data.keys())
        self.assertListEqual(['username', 'password'], error_keys)

    def test_auth_login_endpoint_with_wrong_credentials(self):
        credentials = {
            'username': 'wrong_username',
            'password': 'wrong_password',
        }
        url = reverse('auth-login')
        response = self.client.post(url, data=credentials,
                                    content_type='application/json')
        self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)
        error_keys = list(response.data.keys())
        self.assertListEqual(['non_field_errors'], error_keys)
        self.assertListEqual(['non_field_errors'], error_keys)
        self.assertEqual(response.data['non_field_errors'][0],
                         'Incorrect username/password')
