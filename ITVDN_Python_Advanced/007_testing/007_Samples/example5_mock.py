import datetime
import unittest
import unittest.mock


def sum_two_values(a, b):
    return a + b


def power(x, n):
    return x ** n


def concat_values(*args):
    result = ''
    for item in args:
        result += str(item)
    return result


def desc(x, y):
    if x == 0:
        raise ValueError('`x` should not be equeal 0')
    return y / x


class User:
    def test_method(self):
        raise NotImplementedError


class UserTestCase(unittest.TestCase):

    @unittest.mock.patch('example5_mock.sum_two_values')
    def test_sum_two_values_uncalled(self, mocked_sum):
        # функция нами не вызывалась, а значит called будет False
        self.assertFalse(mocked_sum.called)

    @unittest.mock.patch('example5_mock.sum_two_values')
    def test_sum_two_values_called(self, mocked_sum):
        sum_two_values(10, 20)
        # функция нами вызывалась, а значит called будет True
        # но тело функции не выполнялось, так как мы сделали `mock.patch`.
        self.assertTrue(mocked_sum.called)

    @unittest.mock.patch('example5_mock.sum_two_values')
    def test_sum_two_values_called_with(self, mocked_sum):
        sum_two_values(10, 20)
        self.assertTrue(mocked_sum.called)
        # тело функции выполнялось один раз, проверим это
        self.assertEqual(mocked_sum.call_count, 1)
        # проверим с какими аргументами вызывалась функция
        mocked_sum.assert_called_with(10, 20)

    @unittest.mock.patch('example5_mock.sum_two_values')
    def test_reset_mock(self, mocked_sum):
        sum_two_values(10, 20)
        sum_two_values(10, 20)
        self.assertTrue(mocked_sum.called)
        self.assertEqual(mocked_sum.call_count, 2)
        # проверим вызывалась ли функция используя другой способ
        mocked_sum.assert_called()
        mocked_sum.assert_called_with(10, 20)

        # сбросим счетчик вызовов, после чего функция будет обнулена и
        # все предыдущие вызовы как бы забыты
        mocked_sum.reset_mock()

        self.assertEqual(mocked_sum.call_count, 0)
        self.assertFalse(mocked_sum.called)
        mocked_sum.assert_not_called()

    @unittest.mock.patch('example5_mock.sum_two_values')
    def test_mock_call(self, mocked_sum):
        sum_two_values(10, 40)
        sum_two_values(20, 50)
        sum_two_values(30, 60)
        # был ли хотя бы один вызов функции с такими аргументами
        mocked_sum.assert_any_call(10, 40)

    @unittest.mock.patch('example5_mock.sum_two_values')
    def test_mock_call_with(self, mocked_sum):
        sum_two_values(10, 40)
        mocked_sum.assert_called_with(10, 40)

        sum_two_values(20, 50)
        mocked_sum.assert_called_with(20, 50)

        sum_two_values(30, 60)
        mocked_sum.assert_any_call(30, 60)

    # подменим возвращаемое значение на число 20
    @unittest.mock.patch('example5_mock.sum_two_values', return_value=20)
    def test_mock_return_value_in_dec(self, mocked_sum):
        result1 = sum_two_values(10, 40)
        result2 = sum_two_values(110, 140)
        result3 = sum_two_values(1110, 1140)
        self.assertEqual(result1, 20)
        self.assertEqual(result2, 20)
        self.assertEqual(result3, 20)

    @unittest.mock.patch('example5_mock.sum_two_values')
    def test_mock_return_value_in_body(self, mocked_sum):
        # подменим возвращаемое значение на число 20 используя еще один способ
        mocked_sum.return_value = 20

        result1 = sum_two_values(10, 40)
        result2 = sum_two_values(110, 140)
        result3 = sum_two_values(1110, 1140)
        self.assertEqual(result1, 20)
        self.assertEqual(result2, 20)
        self.assertEqual(result3, 20)

    @unittest.mock.patch('example5_mock.sum_two_values')
    def test_mock_side_effect(self, mocked_sum):
        result = 0

        def res_func(x, y):
            return result

        # по вызову нашей функции мы хотим выполнить сторонний код,
        # который опишем в тесте. Как правило это называется side effect
        mocked_sum.side_effect = res_func

        self.assertEqual(sum_two_values(110, 140), result)
        self.assertEqual(sum_two_values(10, 0), result)
        self.assertEqual(sum_two_values(300, 400), result)

        # мы также можем присвоить экземпляр исключение, чтобы оно было
        # выбрашено в момент вызова
        raise_text = 'Test exception'
        mocked_sum.side_effect = ValueError(raise_text)
        with self.assertRaises(ValueError):
            sum_two_values(10, 30)

        # более того, список исключений для последовательного вызова
        mocked_sum.side_effect = ValueError, RuntimeError, ZeroDivisionError

        with self.assertRaises(ValueError):
            sum_two_values(10, 30)
        with self.assertRaises(RuntimeError):
            sum_two_values(10, 30)
        with self.assertRaises(ZeroDivisionError):
            sum_two_values(10, 30)

        # если мы хотим добавить side effect вместе с возвращаемым значением,
        # которое также хотим задать, используем `return mock.DEFAULT`
        def res_func2(x, y):
            print('Hey')
            return unittest.mock.DEFAULT

        mocked_sum.return_value = 300
        mocked_sum.side_effect = res_func2
        self.assertEqual(sum_two_values(1, 2), 300)

    def test_mock_return_value_in_body_with(self):
        # использование патчинга в связке с оператором with
        with unittest.mock.patch('example5_mock.sum_two_values') as mocked_sum:
            mocked_sum.return_value = 20
            result1 = sum_two_values(10, 40)
            result2 = sum_two_values(110, 140)
            result3 = sum_two_values(1110, 1140)
            self.assertEqual(result1, 20)
            self.assertEqual(result2, 20)
            self.assertEqual(result3, 20)

    def test_mock_builtin(self):
        with unittest.mock.patch('datetime.datetime') as mocked_datetime:
            actual_date = datetime.datetime(2019, 1, 1, 23, 8, 6)

            mocked_datetime.now.return_value = actual_date
            result1 = datetime.datetime.now()
            self.assertEqual(result1, actual_date)

    # мы можем патчить даже методы у классов, используя `mock.patch..object`
    @unittest.mock.patch.object(User, 'test_method')
    def test_user(self, mock_method):
        mock_method.return_value = 10
        user = User()
        # вызываем метод и проверяем наш mock
        user.test_method()
        self.assertTrue(mock_method.called)
        mock_method.assert_called_once()
