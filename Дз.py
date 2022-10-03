#Первое задание

from math import sqrt, cos, sin
a= float(input('Задание 1\n Введите a: '))
b= float(input('Введите b: '))
y = (pow(a, 2)/3) + ((pow(a, 2) + 4)/b) + (sqrt(pow(a, 2+4)) / 4) + (sqrt(pow((pow(a, 2)+4), 3)/4))
print(y)

#Второе задание
x = float(input('Задание 2\n Введите x: '))
y = cos(x) + sin(x)
tg = sin(x)/cos(x)
ctg = cos(x)/sin(x)
print('Y:', y)
print('tg(x)', tg)
print('ctg(x)', ctg)

#Третье задание
x = int(input('Задание 3\n Введите x: '))
y = x**5+x**4+x**3+x**2+x**2+x+1
print('Y:', y)

#Четвертое задание
#a)
x = float(input('Задание 4a\n Введите x: '))
a = float(input('Введите a: '))
y = (0.5 * pow(x, 2))/ (a + x)
print('Y:', y)
#b)
a = float(input('Задание 4b\n Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))
y = (a+b)/(b+(a+c)/(b+c))
print('Y:', y)
#c)
from math import cos,sin
x = float(input('Задание 4c\n Введите x: '))
y= (pow(cos(x**2),2) + pow(sin(x*2-1),2))**1/3
print('Y:', y)
#d)
x = float(input('Задание 4d\n Введите x: '))
y = 5*x+(3*x**3*sqrt(1+(sin(x)**2)))
print('Y:', y)

#Вторая часть
#Первое задание

s = float(input('Задание 1\n Введите сумму кредитования: '))
new_p = float(input('Введите годовые % кредитования: '))
p = new_p/100
n = float(input('Введите количество лет кредитования: '))
m = (s*p*((1+p)**n))/(12*(((1+p)**n)-1))
vsego = m * n * 12
pereplata = vsego - s
print('Ежемесячный платеж составит: ', m)
print('Общая сумма оплаты составит: ', vsego)
print('Сумма переплаты составит: ', pereplata)

#Второе задание
PI = 3.14
R = float(input('Задание 2\nВведите радиус первой планеты: '))
U = float(input('Введите орбитальную скорость первой планеты: '))
y = (2*R*(10**6)*PI)/U
R1 = float(input('Введите радиус второй планеты: '))
U1= float(input('Введите орбитальную скорость второй планеты: '))
y1 =(2*R1*(10**6)*PI)/U1
print('Год на первой планете длинее, чем на второй: ',y>y1)