from models import User


class TestUserModel:
    def setup_method(self, method):
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

    def test_str(self, user, post):
        pass

    def test_full_name(self, user, post):
        pass
