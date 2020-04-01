def get_first_name(self):
    return self.first_name


def get_last_name(self):
    return self.last_name


def get_middle_name(self):
    return self.middle_name


def init(self, first_name, last_name, middle_name):
    self.first_name = first_name
    self.last_name = last_name
    self.middle_name = middle_name


class BaseUser(object):
    def __str__(self):
        return '<user-object/>'


attrs = {
    'first_name': '',
    'last_name': '',
    'middle_name': '',
    'get_first_name': get_first_name,
    'get_last_name': get_last_name,
    'get_middle_name': get_middle_name,
    '__init__': init
}

bases = (
    BaseUser,
)

# создаем класс, используя класс type
# 1. название класса
# 2. классы от которых наследуемся
# 3. набор аттрибутов и методов
User = type('User', bases, attrs)

# вызываем конструктор, который у нас описан функцией `init` выше
user1 = User('John', 'Test', 'Te100vi4')

print(str(user1))
print(user1.get_first_name())
print(user1.get_last_name())
print(user1.get_middle_name())


def build_class(class_name, base_classes, attrs):
    """
    так называемая обёртка над вызовом `type`.
    Позволяет привести все названия атрибутов и методов в нижний регист и
    затем вызывает `type`
    """
    new_attrs = {}
    for attr, value in attrs.items():
        new_attrs[attr.lower()] = value
    return type(class_name, base_classes, new_attrs)
