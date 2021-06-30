"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая объединяет элементы 2 словарей
"""
from copy import deepcopy


def unite_dict(dict_1: dict, dict_2: dict) -> dict:
    dict_1.update(dict_2)
    return dict_1


if __name__ == '__main__':
    assert {1: 100, 2: 200} == unite_dict({1: 100}, {2: 200})
    print('Решено!')
