from random import randint


#DZ 1 С помощью анонимной функции извлеките из списка числа, делимые на 15
n=int(input('Введите кол-во элементов списка: '))
arr = [randint(1,100) for i in range(n)]
print(arr)
print(list(filter(lambda arr: arr % 15== 0,arr)))


#DZ 2 Проверить, все ли числа в последовательности уникальны
#DZ 2.1 Дан список, вывести только уникальные элементы
n=int(input('Введите кол-во элементов списка: '))
arr = [randint(1,100) for i in range(n)]
print(arr)
new_arr = [x for x in arr if arr.count(x) == 1]
if len(arr)>len(new_arr):
    print('Элементы в списке не уникальны')
    print(f'Уникальные элементы списка: {new_arr}')
else:
    print('Элементы списка уникальны')


#DZ 3 Шифр Цезаря
#DZ 3* -шифр цезаря для русских букв тоже
string =input("Set a string: ")
new_string = string.lower()
arr =[]
new_arr = []
x= 0
y = 0
for i in new_string:#Шифровка сообщения и расшифровка
    if ord(i) in range(97,123):
        if ord(i) in range(120,123):
            x= ord(i)
            x-=23
            arr +=chr(x)
        else:
            x = ord(i)
            x +=3
            arr += chr(x)
        if ord(i) in range(97, 100):
            y = ord(i)
            y += 23
            new_arr += chr(y)
        else:
            y = ord(i)
            y -= 3
            new_arr += chr(y)
    elif ord(i) in range(1072,1104):
        if ord(i) in range(1101,1104):
            x = ord(i)
            x-=29
            arr+=chr(x)
        else:
            x = ord(i)
            x+=3
            arr+=chr(x)
        if ord(i) in range(1072, 1075):
            y = ord(i)
            y += 29
            new_arr += chr(y)
        else:
            y = ord(i)
            y -= 3
            new_arr += chr(y)

    else:
        arr+=i
        new_arr+=i

print('Шифровка сообщения:')
print(''.join(arr))
print('Дешифровка сообщения:')
print(''.join(new_arr))
