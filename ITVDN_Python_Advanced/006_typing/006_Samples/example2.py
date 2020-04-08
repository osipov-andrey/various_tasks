# typed
value: int = 10


class User:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


def create_new_user(first_name: str, last_name: str) -> User:
    # автоподстановка first_name.STR_METHODS_AND_PROPS
    print(first_name.upper(), last_name.upper())
    return User(first_name=first_name, last_name=last_name)


user: User = create_new_user('Eugene', 'Test')
