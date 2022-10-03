
#первое задание
a = 5
b = 6
c = 7
print(a + b + c)
print(a - b + c)
print(a * b // c)
print(a * b % c)
print((a ** b / 2) - c * 3)


#второе задание
import math
a= 10
b= 12
print(math.sqrt(a*a+b*b))
print(a*b*0.5)

#третье задание
N = int(input("Введите кол-во дырок для шнурков: "))
a = 5
b = 4
l =  2
nlen = ((N-2)*a) + ((0.5*N)*b) +2*l
print(nlen)


#Задачи на строки
#Первое задание

string = 'Hello World Name Task Time Tools Age'
substring = ' '
count = string.count(substring)
print(count + 1)

#второе задание

string = 'PyCharm'
print(string[2])
print(string[-2])
print(string[0:5])
print(string[:-2])
print(string[0:7:2])
print(string[1:7:2])
print(string[::-1])
print(string[-1::-2])
print(len(string))

#Третье задание
string = 'hello holl house hanter'
print('h' + string[1:-1].replace('h', 'H', 2 ))

#Задачи на вычисления
#Первая задача
a = int(input('Введите число'))
print(a % 10)

#Вторая задача
a = int(input('Введите число'))
print((a % 100)//10)


#Третья задача
a = int(input('Введите трехзначное число'))
print(a // 100 + a % 10 + ((a % 100) //10))