import pytest
from models import User


# фикстура разных уровней
# session - всегда будет одинаковая в рамках сессии
# module - будет одинаковая только в рамках модуля
# class - будет одинаковая в рамках класс
# function - будет одинаковая в рамках функции/метода
@pytest.fixture(scope='session')
# @pytest.fixture(scope='module')
# @pytest.fixture(scope='class')
# @pytest.fixture(scope='function')
# @pytest.fixture
def user():
    return User(
        email='test@example.com',
        first_name='test1',
        last_name='test2',
        fixture=True
    )
