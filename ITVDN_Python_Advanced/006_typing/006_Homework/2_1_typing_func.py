from typing import List


def typing_func(list_elements: List[int]) -> List[str]:
    return [str(i) for i in list_elements]


list_1 = [1, 2, 3, 4, 5]
list_2 = [1, '2', 3]

list_1_res = typing_func(list_1)
list_2_res = typing_func(list_2)
list_3_res = typing_func(3)