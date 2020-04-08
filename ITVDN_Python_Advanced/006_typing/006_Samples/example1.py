# untyped
value = 10


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


def create_new_user(first_name, last_name):
    # неоднозначность типов и преобразований
    # first_name.???
    print(first_name)
    return User(first_name=first_name, last_name=last_name)


# user1 = create_new_user(value, value)
user2 = create_new_user('Test1', 'Test2')
