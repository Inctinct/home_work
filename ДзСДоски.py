#Задание с доски

import math
import time


def decor(func_to_decor):
    def wrapper(*arg):
        start_fun = time.perf_counter_ns()
        func_to_decor(*arg)
        print(f'Затраченное время: {time.perf_counter_ns() - start_fun} наносекунд')
    return wrapper

@decor
def sinus (x):
    summa = 0
    next_part = 1
    eps = 0.0001
    n = 0
    while abs(next_part) > eps:
        next_part = ((-1)**n)*((x**(2*n+1))/(math.factorial(2*n+1)))
        summa += next_part
        n += 1
    print(summa)

@decor
def cosinus(x):
    summa = 0
    next_part = 1
    eps = 0.0001
    n = 0
    while abs(next_part) > eps:
        next_part = ((-1) ** n) * ((x ** (2 * n)) / (math.factorial(2 * n)))
        summa += next_part
        n += 1
    print(summa)
@decor
def exponenta(x):
    summa = 0
    next_part = 1
    eps = 0.0001
    n = 0
    while next_part > eps:
        next_part = (x ** n) / (math.factorial(n))
        summa += next_part
        n += 1
    print(summa)
@decor
def logarifm(x):
    summa = 0
    next_part = 1
    eps = 0.0001
    n = 1
    while abs(next_part) > eps:
        next_part = ((-1) ** (n + 1)) * (x ** n) / n
        summa += next_part
        n += 1
    print(summa)
@decor
def func(x, m):
    summa = 0
    next_part = 1
    eps = 0.0001
    k = 1
    while next_part > eps:
        next_part = (m ** k) * pow(math.log(1 + x),k) / math.factorial(k)
        summa += next_part
        k += 1
    print(summa)


choice = int(input('Выберите функцию:\n1.синус\n2.косинус\n3.(1+x)^m\n4.экспонента\n5.логарифм'))
if choice == 1:
    x = float(input('Введите угол x: '))
    x = math.radians(x)
    sinus(x)

elif choice == 2:
    x = float(input('Введите угол x: '))
    x = math.radians(x)
    cosinus(x)
elif choice == 3:
    x = float(input('Введите х: '))
    m = float(input('Введите m: '))
    func(x,m)

elif choice == 4:
    x = float(input('Введите х: '))
    exponenta(x)

elif choice == 5:
    x = float(input('Введите х: '))
    logarifm(x)



