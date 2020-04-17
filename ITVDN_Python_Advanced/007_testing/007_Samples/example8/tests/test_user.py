import unittest.mock
import unittest
import models


class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.email = 'test@example.com'
        self.first_name = 'test1'
        self.last_name = 'test2'
        self.user = models.User(
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name
        )

    def test_constructor(self):
        self.assertEqual(self.user.first_name, self.first_name)
        self.assertEqual(self.user.last_name, self.last_name)
        self.assertEqual(self.user.email, self.email)

    def test_full_name(self):
        """
        Тестируем метод `.get_full_name()`.
        """
        expected_result = '{first_name} {last_name}'.format(
            first_name=self.first_name,
            last_name=self.last_name,
        )
        full_name = self.user.get_full_name()
        self.assertIsInstance(full_name, str)
        self.assertEqual(full_name, expected_result)

    def test_str(self):
        """
        Проверяем метод __str__, возвращает ли он коррестный тип и значение.
        """
        expected_result = 'User: <{id}: {name}>'.format(
            id=self.user.id,
            name=self.user.get_full_name(),
        )
        str_value = str(self.user)
        self.assertIsInstance(str_value, str)
        self.assertEqual(str_value, expected_result)

    @unittest.mock.patch('models.send_mail')
    def test_send_mail(self, mocked_send_mail):
        """
        Патчим метод отпарвки почты, чтобы в момент тестирования не
        происходило реальной отправки.
        Но как правило надо проверять вызов, то есть мы убеждаемся что письмо
        отпарвляется/не отправляется по вызову нашего метода `send_mail`.
        """
        self.user.send_mail()
        mocked_send_mail.assert_called_once_with(
            self.user.email,
            models.SUBJECT_REGISTRATION.format(name=self.user.get_full_name()),
            models.BODY_REGISTRATION
        )
