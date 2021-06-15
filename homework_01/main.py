"""
Домашнее задание №1
Функции и структуры данныхааааа
"""


def power_numbers(*n):
    k=[]
    for i in n:
        a=i**2
        k.append(a)
    return k
#print(power_numbers(1,2,3))

#rint(power_numbers(2))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers, position) :
    a=[]
    t=0
    if position=="odd":
        for i in numbers:
            if i%2==1:
                a.append(i)
    elif position=='even':
        for i in numbers:
            if i % 2 == 0:
                a.append(i)
    else:
        for i in numbers:
            for d in range(2,i-1):
                if i%d==0:
                    t=+1
            if t==0:
                a.append(i)
    return a
print(filter_numbers([1,2,3,8,10], "prime"))
