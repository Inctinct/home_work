
# Проверка числа на простоту с использованием рекурсии
def rec(number,divider):
    if divider == 1:
        return True
    if number % divider == 0:
        return False
    else:
        return rec(number,divider-1)


number = int(input("Set a number: "))
divider = number -1
print(f'Число простое? {rec(number,divider)}')




#Нахождение наибольшего общего делителя (НОД) при помощи рекурсии
def recur(number1,number2):
    if number2 == 0:
        return number1
    else:
        return recur(number2,number1 % number2)

number1 = int(input("Set a number1: "))
number2 = int(input("Set a number2: "))
print(recur(number1,number2))


"""
Шифр Виженера
"""
def encryption(Alphabet,key):
    arr = []
    n = 0
    for i in message:
        arr += Alphabet[((Alphabet.index(i) + Alphabet.index(key[n])) % 26)]
        n += 1
        if n == len(key):
            n = 0
    return ''.join(arr)


def decryption(Alphabet,key):
    arr = []
    n = 0
    for i in message:
        arr += Alphabet[((Alphabet.index(i) - Alphabet.index(key[n])) % 26)]
        n += 1
        if n == len(key):
            n = 0
    return ''.join(arr)
Alphabet ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
message = input('Set a message: ').upper()
key = input('Set a key: ').upper()
print(f'Encryption: {encryption(Alphabet,key)}')
print(f'Decryption: {decryption(Alphabet,key)}')



"""
Выполнить обработку элементов прямоугольной матрицы А, имеющей N строк и М столбцов.
 Найти сумму элементов всей матрицы.
 Определить, какую долю в этой сумме составляет сумма элементов каждого столбца. 
 Результат оформить в виде матрицы из N+1 строк и M столбцов.
"""

from random import randint
matrix = []
summa = 0
result = 0
arr = []
N = int(input('Set number of lines: '))
M = int(input('Set number of columns: '))
for i in range(0,N):
    matrix.append([])
    for j in range(0,M):
        matrix[i].append(randint(0,50))
        summa+= matrix[i][j]

    print(matrix[i])

for j in range(0,M):
    result = 0
    for i in range(0,N):
        result+=matrix[i][j]

    procent = (result / summa *100)
    arr.append(round(procent))

print(arr)
print(summa)


from random import randint
matrix=[]
N = int(input('Set number of lines: '))
M = int(input('Set number of columns: '))
for i in range(0,N):
    matrix.append([])
    for j in range(0,M):
        matrix[i].append(randint(0,50))


    print(matrix[i])

"""
Выполнить обработку элементов прямоугольной матрицы А, имеющей N строк и М столбцов.
Перемножить элементы каждого столбца матрицы с соответствующими элементами K-го столбца.
"""
new_matrix = []
K= int(input('Set a number of K colum: '))
for i in range(0,N):

    new_matrix.append([])
    for j in range(0,M):
        new_matrix[i].append(matrix[i][j]*matrix[i][K])
    print(new_matrix[i])

"""
Выполнить обработку элементов прямоугольной матрицы А, имеющей N строк и М столбцов.
Просуммировать элементы каждой строки матрицы с соответствующими элементами L - той строки.

"""
new_matrix= []
L=int(input('Set a number of L line: '))
for i in range(0,N):
    new_matrix.append([])
    for j in range(0,M):
        new_matrix[i].append(matrix[i][j]+matrix[L][j])
    print(new_matrix[i])
"""
Выполнить обработку элементов прямоугольной матрицы А, имеющей N строк и М столбцов. Все элементы имеют целый тип.
Дано целое число Н. Определить, какие столбцы имеют хотя бы одно такое число, а какие не имеют.
"""
H = int(input('Set integer number: '))
for i in range(0,N):
    for j in range(0,M):
        if matrix[i][j] == H:
            print(f'Colum {j+1} have a {H}')
        else:
            continue

"""
Выполнить обработку элементов квадратной матрицы А, имеющей N строк и N столбцов.
Найти сумму элементов, стоящих на главной диагонали, и сумму элементов, стоящих на побочной диагонали.

Выполнить обработку элементов квадратной матрицы А, имеющей N строк и N столбцов.
Определить сумму элементов, расположенных параллельно главной диагонали (ближайшие к главной).


Выполнить обработку элементов квадратной матрицы А, имеющей N строк и N столбцов.
Определить произведение элементов, расположенных параллельно побочной диагонали (ближайшие к побочной).
"""


if N==M:
    result1 = 0
    result2 = 0
    i=0
    j=0
    while i!=N:
        result1+=matrix[i][j]
        i+=1
        j+=1
    print(f'Summa of a main diagonal = {result1}')

    i=N-1
    j=0
    while j!=N:
        result2+=matrix[i][j]
        i-=1
        j+=1
    print(f'Sumaa of a secondary diagonal = {result2}')
    result1=0
    result2=0
    i=1
    j=0
    while i!=N:
        result1+=matrix[i][j]
        i+=1
        j+=1
    i=0
    j=1
    while j!=N:
        result2+=matrix[i][j]
        i+=1
        j+=1
    print(f'Summa of a diagonals parallel to the main = {result1+result2}')
    result1=1
    result2=1
    i=N-1
    j=1
    while j!=N:
        result1*=matrix[i][j]
        i-=1
        j+=1
    i=N-2
    j=0
    while i!=-1:
        result2*=matrix[i][j]
        i-=1
        j+=1
    print(f'Multiplication of a diagonal parallel side = {result1 * result2}')

"""
Выполнить обработку элементов прямоугольной матрицы А, имеющей N строк и М столбцов.
Исходная матрица состоит из нулей и единиц.
Добавить к матрице еще один столбец, каждый элемент которого делает количество единиц в каждой строке четным.

"""
from random import randint
count=0
matrix=[]
N = int(input('Set number of lines: '))
M = int(input('Set number of columns: '))
for i in range(0,N):
    matrix.append([])
    for j in range(0,M):
        matrix[i].append(randint(0,1))
    if matrix[i].count(1) % 2 == 1:
        matrix[i].append(1)
    else:
        matrix[i].append(0)
    print(matrix[i])


"""
Выполнить обработку элементов прямоугольной матрицы А, имеющей N строк и М столбцов. 
Дан номер строки L и номер столбца К, при помощи которых исходная матрица разбивается на четыре части. 
Найти среднее арифметическое элементов каждой части.

"""
from random import randint
count=0
matrix=[]
N = int(input('Set number of lines: '))
M = int(input('Set number of columns: '))
for i in range(0,N):
    matrix.append([])
    for j in range(0,M):
        matrix[i].append(randint(0,50))
    print(matrix[i])

L=int(input('Set a number of L line: '))
K= int(input('Set a number of K colum: '))
result1,result2,result3,result4 =0,0,0,0
count1,count2,count3,count4=0,0,0,0
for i in range(0,N):
    if i < L:
        for j in range(0,M):
            if j <K:
                result1+=matrix[i][j]
                count1+=1
            if j > K:
                result2+=matrix[i][j]
                count2+=1
    if i > L:
        for j in range(0,M):
            if j <K:
                result3+=matrix[i][j]
                count3+=1
            if j > K:
                result4+=matrix[i][j]
                count4+=1
print(f'arithmetic mean first part = {result1/count1}')
print(f'arithmetic mean second part = {result2/count2}')
print(f'arithmetic mean third part = {result3/count3}')
print(f'arithmetic mean fourth part = {result4/count4}')

"""
Заполнение по спирали
"""
matrix=[]
N = int(input('Set number of lines: '))
M=N
value=N*N
K=M//2
for i in range(0, N):
    matrix.append([])
    for j in range(0, M):
        matrix[i].append(0)

i=0
j=0
while N!=0:
    it=0
    while it<N-1:
        matrix[i][j]=value
        value-=1
        j+=1
        it+=1
    for it in range(0,N-1):
        matrix[i][j]=value
        value-=1
        i+=1
    for it in range(0,N-1):
        matrix[i][j]=value
        value-=1
        j-=1
    for it in range(0,N-1):
        matrix[i][j]=value
        value-=1
        i-=1
    i+=1
    j+=1

    if N<2:
        N=0
        matrix[K][K]=value
    else:
        N=N-2

for i in range(0,M):
    for j in range(0,M):

        print(matrix[i][j], end=' ' * 3)
    print()


"""
Бинарный поиск
"""


arr=[i for i in range(1,100)]
value = int(input('Set a Value: '))

mid = len(arr) // 2
low = 0
high = len(arr) - 1

while arr[mid] != value and low <= high:
    if value > mid:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("No value")
else:
    print(f'ID = {mid}')

"""
Бинарный поиск со сдвигом
"""
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



