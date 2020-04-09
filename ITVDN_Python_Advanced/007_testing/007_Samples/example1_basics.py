import unittest


def test_function(value):
    return value * 20


class UserTestCase(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(2 + 2, 4)

    def test_multiply(self):
        self.assertTrue(2 * 4 == 8)

    def test_test_function(self):
        value = 100
        self.assertEqual(test_function(value), value * 20)

    def test_test_function_wrong(self):
        value = 100
        self.assertEqual(test_function(value), value * 30)
