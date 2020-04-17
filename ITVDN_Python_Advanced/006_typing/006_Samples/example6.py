from typing import TypeVar, List, Tuple, Sequence, Iterable

T = TypeVar('T')


def copy_list(sequence: Iterable[Tuple[str, T]]) -> List[T]:
    new_list: List[T] = []
    for elem in sequence:
        new_list.append(elem[1])
    return new_list


test_data = [
    ('1', 10),
    ('1', 10),
    ('1', '1'),
]
test_value0 = copy_list(test_data)
# test_value1 = copy_list([1, 2, 3])
# test_value2 = copy_list([1, 2, 9])
# test_value3 = copy_list([1.3, 2.1, 3])
# test_value4 = copy_list(["srt", "rts", "str"])
# test_value5 = copy_list(("srt", "rts", "str"))
# test_value6 = copy_list({"srt", "rts", "str"})
