class LinkedList:

    def __init__(self, first_node):
        self.first_node = first_node

    def __iter__(self):
        return LinkedListIterator(self)

    def print_list(self):
        for node in self:
            print(f"node: {node} => next node: {node.next}")

    def reverse(self):
        prev_node = None
        for node in self:
            node.next = prev_node
            prev_node = node
        self.first_node = prev_node


class LinkedListIterator:

    def __init__(self, linked_list_):
        self._counter_to_node = linked_list_.first_node

    def __iter__(self):
        return self

    def __next__(self):
        next_node = None
        if self._counter_to_node is None:
            raise StopIteration
        try:
            next_node = self._counter_to_node.next
            return self._counter_to_node
        finally:
            self._counter_to_node = next_node


class Node:

    def __init__(self, next_node=None):
        self._next_node = next_node

    def __str__(self):
        return str(id(self))

    @property
    def next(self):
        return self._next_node

    @next.setter
    def next(self, node):
        self._next_node = node


def generate_linked_list(length=10):
    first_node = Node()
    current_node = first_node
    for _ in range(length - 1):
        new_node = Node()
        current_node.next = new_node
        current_node = new_node
    return LinkedList(first_node)


if __name__ == '__main__':
    linked_list = generate_linked_list()
    linked_list.print_list()
    linked_list.reverse()
    print("Reversed: \n")
    linked_list.print_list()
