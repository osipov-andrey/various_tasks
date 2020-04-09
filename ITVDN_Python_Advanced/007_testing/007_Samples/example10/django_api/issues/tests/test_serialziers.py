from django.test import TestCase
from django.contrib.auth.models import User

from issues.serializers import LoginSerializer


class LoginSerializerTestCase(TestCase):

    def setUp(self):
        self.username = 'test'
        self.password = 'pass1234'
        self.user = User.objects.create_user(
            first_name='Test',
            last_name='Testovich',
            username=self.username,
            password=self.password,
            email='test@example.com'
        )

    def test_validate_with_wrong_credentials(self):
        credentials = {
            'username': 'test1',
            'password': 'pass'
        }
        serializer = LoginSerializer(data=credentials)
        self.assertFalse(serializer.is_valid())
        self.assertGreater(len(serializer.errors), 0)
        self.assertRegex(serializer.errors['non_field_errors'][0],
                         'Incorrect username\/password')

    def test_validate_without_password(self):
        credentials = {
            'username': 'test1',
        }
        serializer = LoginSerializer(data=credentials)
        self.assertFalse(serializer.is_valid())
        self.assertIn('password', serializer.errors)
        self.assertRegex(serializer.errors['password'][0],
                         'required')

    def test_validate_without_username(self):
        credentials = {
            'password': 'pass',
        }
        serializer = LoginSerializer(data=credentials)
        self.assertFalse(serializer.is_valid())
        self.assertIn('username', serializer.errors)
        self.assertRegex(serializer.errors['username'][0],
                         'required')

    def test_validate(self):
        credentials = {
            'username': self.username,
            'password': self.password,
        }
        serializer = LoginSerializer(data=credentials)
        self.assertTrue(serializer.is_valid())
        self.assertIsInstance(serializer.validated_data, User)
