"""
Домашнее задание №1
Функции и структуры данныхааааа
"""


def power_numbers(n):
    spisok=[]
    for i in n:
        k=i**2
        spisok.append(k)
    return spisok
#print(power_numbers([1,2,3]))


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
