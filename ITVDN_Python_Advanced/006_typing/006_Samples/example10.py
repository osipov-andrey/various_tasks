from typing import TypeVar, Dict, ClassVar


class User:
    meta: ClassVar[Dict[str, int]]

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


user = User('test1', 'test2')
# user.meta = {}
User.meta = {}


class A:
    def foo(self, instance: 'B'):
        pass


class B:
    def foo(self, instance: 'A'):
        pass


a1 = A()
b1 = B()

b1.foo(a1)
a1.foo(b1)
# a1.foo(a1)
