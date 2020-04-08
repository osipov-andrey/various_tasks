from typing import Dict, Tuple, List


def generate_tuple(data) -> list:
    result = []
    for key, value in data.values():
        result.append((key, value))
    return result


test_data1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
test_data2 = {'k1': 'v1', 'k2': 'v2', 'k3': 10}
test_data3 = {'k1': 'v1', 'k2': 'v2', 'k3': 10.4}
test_data4 = {'k1': 'v1', 'k2': 'v2', 'k3': []}

test_value1 = generate_tuple(test_data1)  # type: Tuple[str, str]
test_value2 = generate_tuple(test_data2)  # type: Dict[str, int]
test_value3 = generate_tuple(test_data3)  # type: List
test_value4 = generate_tuple(test_data4)  # type: dict

another_value = '10'  # type: str
# test_value1.???
# test_value2.???
# test_value3.???
# test_value4.???
