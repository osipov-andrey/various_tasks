
def build_class(class_name, base_classes, attrs):
    new_attrs = {}
    for attr, value in attrs.items():
        new_attr = attr.lower()
        new_attrs[new_attr] = value
    return type(class_name, base_classes, new_attrs)


class BaseClass(object):
    def __str__(self):
        return '<user-object/>'


class_name = "MyClass"
base_classes = (BaseClass,)


def method_1():
    print("I'm a method!")


def method_2(self):
    return self.attr_2


# def init(self, attr_1, attr_2):
#     self.attr_1 = attr_1
#     self.attr_2 = attr_2


attrs = {
    "ATTR_1": 1,
    "attr_2": "two",
    "meThod_1": method_1,
    "method_2": method_2,
    # "__init__": init
}

new_class = build_class(class_name, base_classes, attrs)

obj_new_class = new_class()

print(obj_new_class.method_2())
# new_class.method_1()
# print(new_class.method_2(new_class))
#
# new_class_2 = type("MyClass", base_classes, attrs)
#
# print(new_class_2.method_2(new_class_2))