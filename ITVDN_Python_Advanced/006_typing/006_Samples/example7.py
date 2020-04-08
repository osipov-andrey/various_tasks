from typing import Callable


def handler(name: str, coefficient: int) -> None:
    print(name)
    print(coefficient)


def incorrect_handler(value: str, coefficient: int):
    print(value)


def executor(value1: str, value2: int, callback: Callable[[str, int], None]):
    callback(value1, value2)


executor("Test string", 10, handler)
executor("Test string", 10, incorrect_handler)
