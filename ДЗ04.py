import math
import time

def decor(func_to_decor):
    def wrapper():
        start_time = time.time()
        func_to_decor()
        print("______%s seconds______" % (time.time() - start_time))

    return wrapper

@decor
def first():
    x = 0.6
    summa = 0
    res = 0
    while x<= 1.1:
        for n in range(10, 16):
            for k in range(1, n + 1):
                summa += pow(math.log(abs(x + k)), 2) * ((math.cos(k + pow(math.sin(x), 1 / 5))) / (k * x))
            res += (1 / 45 * math.sqrt(3 ** (x + n))) * summa
            print(f"{x=}, {n=}, {res=}")
        x+=0.25
    print(round(res, 2))
@decor
def second():
    exp = 2.718
    x = 0.6
    PI = 3.14
    summa = 0
    res = 0
    while x <= 1.1:
        for n in range(10, 16):
            for k in range(1, n + 1):
                summa += (math.sqrt((pow((x ** (k + 1)), 1 / k)) + (pow((exp ** (k - 2 / 3)), k)))) / (
                            1 + math.log10(x))
            res += math.sin((PI * n) / (x + 3)) * summa
            print(f"{x=}, {n=}, {res=}")
        x+=0.25
    print(round(summa, 2))
@decor
def third():
    exp = 2.718
    x = 0.6
    summa = 0
    res = 0
    while x <= 1.1:
        for n in range(10, 16):
            for k in range(1, n + 1):
                summa += (1 + ((k + 1) / n)) / (((pow(exp, k)) * (pow(pow(x, k - 1), 1 / 2))) + (math.log10(x)))
            res += (math.sqrt(pow(math.sin(x / n), 3))) * summa
            print(f"{x=}, {n=}, {res=}")
        x+=0.25
    print(round(summa, 2))
@decor
def fourth():
    exp = 2.718
    x = 0.6
    PI = 3.14
    summa = 0
    res = 0
    while x <= 1.1:
        for n in range(10, 16):
            for k in range(1, n + 1):
                summa += (pow(math.sin((k - 1) / (k + 1)), 2)) + (exp ** math.sqrt(x / k))
            res += (PI / ((x ** (1 / 3)) + (3 / (x + 5)))) * summa
            print(f"{x=}, {n=}, {res=}")
        x += 0.25
    print(round(summa, 2))

enter = 1
while enter ==1:
    number= int(input('Выберите номер примера:1 2 3 4'))
    if number == 1:
        first()
    elif number == 2:
        second()
    elif number ==3:
        third()
    elif number ==4:
        fourth()
    enter =int(input('Желаете продолжить?: 1.да 2.нет'))