from typing import List, Union

import unittest.mock
import random
import math


def average(list_: List[Union[float, int]]) -> float:
    if len(list_) == 0:
        raise ValueError("List is empty")
    return sum(list_) / len(list_)


def remove_x(list_: list, x):
    while 1:
        try:
            list_.remove(x)
        except ValueError:
            break


def send_email(first_name: str, last_name: str, birthday: str):
    message = f"Created new user {first_name} {last_name}. " \
              f"Birthday: {birthday}"
    print(message)


def create_user(first_name: str, last_name: str, birthday: str):
    # creating...
    send_email(first_name, last_name, birthday)


class AverageTest(unittest.TestCase):

    def test_1(self):
        for _ in range(1000):
            len_ = random.randint(20, 30)
            list_ = [random.randint(0, 100) / random.randint(1, 10) for i in range(len_)]
            result_test = sum(list_) / len_
            result_func = average(list_)
            self.assertEqual(result_test, result_func)

    def test_2(self):
        with self.assertRaises(ValueError):
            average([])
            raise ValueError


class RemoveXTest(unittest.TestCase):

    def test_1(self):
        for _ in range(1000):
            len_ = random.randint(50, 100)
            list_ = [random.randint(0, 100) for i in range(len_)]
            x = random.choice(list_)
            remove_x(list_, x)
            self.assertNotIn(x, list_)

    def test_2(self):
        for _ in range(1000):
            def take_type(val):
                return random.choice((str(val), int(val)))

            len_ = random.randint(50, 100)
            list_ = [take_type(random.randint(0, 100)) for i in range(len_)]
            x = random.choice(list_)
            remove_x(list_, x)
            self.assertNotIn(x, list_)


class CreateUserTest(unittest.TestCase):

    @unittest.mock.patch('1_1_task_1-2-3.send_email')
    def test_create_user(self, mocked_email):
        create_user('test', 'test', 'test')
        self.assertTrue(mocked_email.called)
