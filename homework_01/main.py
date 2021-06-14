"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(n):
    n=[]
    for i in n:
        nvkvadrate=i**2
        n.append(nvkvadrate)
    return(n)

power_numbers(2,3)





# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers():
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
