import pytest
from models import Post


def pytest_runtest_setup(item):
    print('SetUp', item)


@pytest.fixture(scope='session')
# @pytest.fixture(scope='module')
# @pytest.fixture(scope='class')
# @pytest.fixture(scope='function')
# @pytest.fixture
def post(user):
    return Post(
        user=user,
        comment='Test Comment',
        fixture=True
    )
