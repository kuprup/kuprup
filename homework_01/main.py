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
    c=[]
    t=0
    indx=int
    numbers.sort()
    if position=="odd":
        for i in numbers:
            if i%2!=0:
                a.append(i)
    elif position=='even':
        for i in numbers:
            if i % 2 == 0:
                a.append(i)
    else:
        for i in numbers:
            for s in range(2,i+1):
                if i%s==0 and i>s:
                    break
            else:
                a.append(i)
    return a
print(filter_numbers([1,2,3,8,10, 91], "odd"))
