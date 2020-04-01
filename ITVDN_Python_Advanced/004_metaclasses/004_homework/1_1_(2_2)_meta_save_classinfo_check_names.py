import re
from collections import OrderedDict


class HigherWordsInNameException(Exception):
    pass


class DigitsInNameException(Exception):
    pass


class BaseMeta(type):

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print('Prepared', name, bases, kwargs)
        return OrderedDict()

    @staticmethod
    def __new__(mcs, name, bases, attrs):
        print('mcs', mcs)
        new_attrs = OrderedDict()
        for key, value in attrs.items():
            key_lower = key.lower()
            if key_lower != key:
                raise HigherWordsInNameException(key)
            elif re.search(r'\d', key):
                raise DigitsInNameException(key)



        new_cls = super().__new__(mcs, name, bases, attrs)
        class_name = new_cls.__name__
        class_qual_name = new_cls.__qualname__
        class_metadata = new_cls.__dict__
        class_mro = new_cls.__mro__
        print("Class Name: ", class_name)
        print("Class Qualname: ", class_qual_name)
        print("Class Metadata: ", class_metadata)
        print("Class MRO: ", class_mro)
        return new_cls


def get_first_name(self):
    return self.first_name


class BaseUser(object):
    def __str__(self):
        return '<user-object/>'


bases = (
    BaseUser,
)


class NewClass(BaseUser, metaclass=BaseMeta):
    get_first_name = get_first_name
    bases = bases
    first_attr = 1
    second_attr = 2

    def __init__(self, first_name):
        self.first_name = first_name


obj = NewClass("Andrey")
print(obj)
print(obj.get_first_name())