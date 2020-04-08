from typing import Dict, Tuple, List

# dict, состоящий из строковых ключей и float в качестве значений
test_value: Dict[str, float] = {
    'v1': 10.2,
    'v2': 10.2,
    'v3': 10.2,
    # 'v4': 'test string',
    # 'v5': ['test string'],
}


def generate_tuple(data: Dict[str, str]) -> List[Tuple[str, str]]:
    result = []
    for key, value in data.items():
        result.append((key, value))
    return result


test_data1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
test_data2 = {'k1': 'v1', 'k2': 'v2', 'k3': '10'}
test_data3 = {'k1': 'v1', 'k2': 'v2', 'k3': '10.4'}
test_data4 = {'k1': 'v1', 'k2': 'v2', 'k3': '[]'}

test_value1 = generate_tuple(test_data1)
test_value2 = generate_tuple(test_data2)
test_value3 = generate_tuple(test_data3)
test_value4 = generate_tuple(test_data4)
