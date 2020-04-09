import json
import os
import uuid
from typing import ClassVar


class Counter:
    counter: ClassVar[int] = 0

    def __init__(self, fixture):
        if fixture:
            self.update_counter()

    def update_counter(self):
        self.__class__.counter += 1
        name = self.__class__.__name__.lower()
        data = {}
        if os.path.exists('results.json'):
            with open('results.json', 'r') as f:
                data = json.load(f)
        data.setdefault(name, 0)
        data[name] += 1
        with open('results.json', 'w') as f:
            json.dump(data, f)


class User(Counter):

    def __init__(self, email, first_name, last_name, uid=None, fixture=False):
        super().__init__(fixture)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = uid or uuid.uuid4()

    def get_full_name(self):
        return '{first_name} {last_name}'.format(
            first_name=self.first_name,
            last_name=self.last_name
        )

    def __str__(self):
        return 'User: <{id}: {name}>'.format(
            id=self.id,
            name=self.get_full_name()
        )


class Post(Counter):

    def __init__(self, user, comment: str, fixture=False):
        super().__init__(fixture)
        self.user = user
        self.comment = comment
