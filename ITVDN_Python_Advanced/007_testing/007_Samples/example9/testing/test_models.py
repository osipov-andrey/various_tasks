import datetime

from models import User


def setup_method(self, method):
    raise ValueError


class TestUserModel:
    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_constructor(self):
        user = User('e@example.com', 't1', 't2')
        assert user.first_name == 't1'
        assert user.last_name == 't2'
        assert user.email == 'e@example.com'

    def test_str(self, user):
        pattern = 'User: <{id}: {name}>'
        assert str(user) == pattern.format(id=user.id,
                                           name=user.get_full_name())

    def test_full_name(self, user):
        pattern = '{} {}'
        assert user.get_full_name() == \
               pattern.format(user.first_name, user.last_name)


class TestUserModel2:

    def test_constructor(self):
        user = User('e@example.com', 't1', 't2')
        assert user.first_name == 't1'
        assert user.last_name == 't2'
        assert user.email == 'e@example.com'

    def test_str(self, user):
        pattern = 'User: <{id}: {name}>'
        assert str(user) == pattern.format(id=user.id,
                                           name=user.get_full_name())

    def test_full_name(self, user):
        pattern = '{} {}'
        assert user.get_full_name() == \
               pattern.format(user.first_name, user.last_name)

    def test_list(self):
        assert [1, 2, 3] == [1, 2, 3]
        # assert [1, 2, 3] == [1, 2, 4]

    def test_mocker(self, mocker):
        mocked_dt = mocker.patch('datetime.datetime')
        mocked_dt.now.return_value = 1
        assert datetime.datetime.now() == 1
        assert [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 20, 3, 4, 5] == \
               [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
