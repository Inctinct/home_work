#Написать filter  с лямбда-функцией определяющей число чётное/нечётное.
""""""
arr = []
n = int(input("Введите кол-во элементов: "))
for i in range(n):
    arr.append(int(input('Введите элемент: ')))
print(list(filter(lambda arr : arr % 2 == 0,arr )))
#Дан список. Сделать список с помощью функции map, которая переводит каждое число из исходного списка в строку
arr = [1,2,3,4]
print(list(map(lambda arr: str(arr), arr )))
"""С помощью функции filter отфильтровать из исходного списка строк только те строки,
 которые являются палиндромами. Палиндром - в обе стороны читается одинаково. ‘abccba’ - палиндром например"""
arr = ['aa','ab', 'abccba']
arr1 =[]
print(list(filter(lambda arr: arr == arr[::-1], arr)))
#Дан словарь, вывести новый словарь, поменяв местами ключи со значениями из исходного словаря
dict = {'dog': 'Собака', 'cat':'Кот'}
new_dict = {val:key for key,val in dict.items()}
print(new_dict)
#Написать функцию для нахождения факториала числа. Две реализации: через рекурсию и без рекурсии
def rec_fact(x):
    if x ==1:
        return x
    else:
        return x*rec_fact(x-1)

x = int(input('Введите число: '))
print(rec_fact(x))

def fact(x):

    fac = 1
    if x ==1:
        return x
    else:
        while x > 1:
            fac *= x
            x -=1
    return fac
x = int(input('Введите чичло: '))
print(fact(x))
"""еще задача на циклы: сделать угадайку числа для пользователя.
Загадываете рандомное число, у юзера 10 попыток. 
У юзера после каждого выигрыша/проигрыша должен быть выбор продолжить игру или нет. 
Если продолжить - рандомите новое число и угадываете снова, если нет - завершаете программу"""
from random import randint
n = 0
game = 1
while game == 1:
    n = 0
    x = int(input('Введите начальный диапозон числа: '))
    y = int(input('Введите конечный диапозон числа: '))
    while n < 10:
        x = randint(x, y)
        a= int(input(f" Попытка №{n+1} Введите число: "))
        if a != x:
            print("Неверное число")
            n += 1
        elif a == x:
            print('Вы угадали число')
            game = int(input('Желаете продолжить игру?\n1.Да\n2.Нет'))
            if game == 1:
                n =10
            else:
                break


