# from math import sqrt
# a= int(input())
# b= int(input())
# y = (pow(a, 2)/3) + ((pow(a, 2) + 4)/b) + (sqrt(pow(a, 2+4)) / 4) + (sqrt(pow((pow(a, 2)+4), 3)/4))
# print(y)

"""
from math import pow, sin, cos
a = float(input())
x = float(input())
y = 3 * (pow((x + 10 * pow(a, 7))/(sin(x) + (cos(a)) ** 3), 1/5))
print(y)

import math

summa = 0
next_part = 1
eps = 0.0001
n = 0
x = float(input('Set agnle in degrees:'))
x= math.radians(x)

while abs(next_part) > eps:
    next_part = (-1) ** n * ((x**(2*n+1))/(math.factorial(2*n+1)))
    summa += next_part
    n += 1

print(f'Sin: {summa} ')

from math import cos
x = 0.6
exp =  2.718
while x < 1.1:
    summa = 0
    for n in range(10,16):
        for k in range(0, n+1):
            summa =+ cos(x*k)
        res = exp**x +summa
        print(f"{x=}, {n=}, {res=}")

    x+= 0.25


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


def rec(sl, search):
    if search in sl.keys():
        return sl[search]
    for n in sl.values():
        if type(n) == dict:
            ret = rec(n, search)
            if ret != None:
                return ret
print(rec(title, input('Enter \n')))





print(1)
print(1)


def fib(n):
    fib=1
    new_fib=1
    num =0
    while num<n-2:
        fib= fib+new_fib
        print(fib)
        new_fib +=fib
        print(new_fib)
        num+=2

fib(5)





def fib(n):
    f1=f2=1
    print(f1,f2, end='')
    for i in range(2, n-1):
        temp=f1
        f1=f2
        f2=temp+f1
        print(f2, end='')


nums= [1,3,2,4,5]
def func(nums):
    myMax = nums[0]
    myMin = nums[0]
    for i in range(len(nums)):
        if i > myMax:
            myMax = i
        if i < myMin:
            myMin = i
    print(myMax-myMin)


func(nums)

import string


class Alphabet():
    def __init__(self,language, letters_str):
        self.lang=language
        self.letters=list(letters_str)

    def print(self):
        print(self.letters)

    def letters_num(self):
        len(self.letters)


class EngAlphabet():
    __letters_num = 26

    def __init__(self):
        super().__init__('En',string.ascii_uppercase)

    def is_en_letter(self,letter):
        if letter.upper() in self.letters:
            return True
        return False

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        print("English Example:\nDon't judge a book by it's cover.")

if __name__ == '__main__':
    eng_alphabet = EngAlphabet()
    eng_alphabet.print()
    print(eng_alphabet.letters_num())
    print(eng_alphabet.is_en_letter('F'))
    print(eng_alphabet.is_en_letter('Щ'))
    EngAlphabet.example()


def rec(number):
    if number == 0:
        return
    else:
        arr.append(number % 2)
        return rec(number//2)

number = int(input('Set a number:'))
arr = []
rec(number)
arr.reverse()
print(arr)

matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]

matrix =[]
N=M=3
for i in range(0,N):
    matrix.append([])
    for j in range(0,M):
        matrix[i].append(0)
    print(matrix[i])

matrix = [[0]*M for i in range(N)]
print(matrix)
for row in matrix:
    print(row)
for i in range(0,N):
    for j in range(0,M):
        if i == j:
            matrix[i][j]=1
for row in matrix:
    print(row)

from random import randint
matrix = []
M=N=5
for i in range(0,N):
    matrix.append([])
    for j in range(0,M):
        matrix[i].append(randint(0,50))
    print(matrix[i])

myMax = matrix[0][0]
myMin = matrix[0][0]
for i in range(0,N):
    for j in range(0,M):
        if matrix[i][j] > myMax:
            myMax = matrix[i][j]
        if matrix[i][j] < myMin:
            myMin = matrix[i][j]
print(myMax)
print(myMin)

print('Input n --> ')

# 6 - квадратная спираль снаружу
n = int(input())

v = [[0] * n for i in range(n)]
m = n

i = 0
j = n - 1
value = n * n

while n != 0:
    k = 0
    while k < n - 1:
        value -= 1
        j -= 1
        v[i][j] = value
        k += 1
    for k in range(0, n - 1):
        i += 1
        value -= 1
        v[i][j] = value
    for k in range(0, n - 1):
        j += 1
        value -= 1
        v[i][j] = value
    for k in range(0, n - 1):
        i -= 1
        value -= 1
        v[i][j] = value
    i += 1
    j -= 1
    if n < 2:
        n = 0
    else:
        n = n-2


for i in range(m):
    for j in range(m):
        print(v[i][j], end=' ' * 3)
    print()

matrix=[]
N = int(input('Set number of lines: '))
for i in range(0, N):
    matrix.append([])
    for j in range(0, N):
        matrix[i].append(0)
K=N//2
value=1
count=0
step = 1

i,j=K,K
while value !=N*N+1:
    while count != step:
        value+=1
        i-=1
        matrix[i][j]=value
        print(matrix[i][j])
        value+=1
        j+=1
        matrix[i][j]=value
        print(matrix[i][j])
        count+=1
    step+=1
    count=0

for i in range(0,N):
    for j in range(0,N):

        print(matrix[i][j], end=' ' * 3)
    print()



arr=[i for i in range(1,100)]
shift = int(input('Set a shift: '))
value = int(input('Set a Value: '))
arr = arr[-shift:] + arr[:-shift]
print(arr)

if value <= len(arr)-1:

    if value <= arr[shift-1] and value >= arr[0]:
        low = arr[0]
        high = arr[shift - 1]
        mid = (arr[0] + arr[shift - 1]) // 2

        while mid !=value:
            if value > mid:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2

    elif value >=arr[shift] and value<= arr[len(arr)-1]:
        low = arr[shift]
        high=arr[len(arr)-1]
        mid = (arr[len(arr)-1]-arr[shift])//2

        while mid !=value and low<=high:
            if value > mid:
                low = mid+1
            else:
                high = mid-1
            mid = (low + high) // 2

    print(arr.index(mid))
else:
    print('No Value')



arr=[]
f1=open('example1.txt','w')
f1.close()
string=''
f = open('example.txt','w')
f.write('12345')
f.close()
with open('example.txt') as f:
    for i in f:
        arr.append(i)
print(arr)
with open('example1.txt','w')as f1:
    f1.write(''.join(arr[::-1]))
"""
import csv
import json


with open('data_file.json', 'r') as f:
    data = json.loads(f.read())
cols =['name','birthday','height','weight','car','languages']
with open('some.csv', 'w',newline='') as f:
    wr = csv.DictWriter(f, fieldnames = cols)
    wr.writeheader()
    wr.writerows(data)

with open('data_file.json', 'r') as f:
    data = json.loads(f.read())



