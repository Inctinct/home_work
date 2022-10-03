string = input("Set a string: ")

def digit(string):
    if string.isdigit() == True:
        string = int(string)
        print(f'Вы ввели положительное целое число: {string}')
    else:
        for arr in string:
            if arr.isdigit() == False:
                if arr != '.' and arr != '-':
                    print(f'Неверное число: {string}')
                    exit(0)
        for arr in string:
            if arr == '.':
                string = float(string)
        if isinstance(string, float):
            if string < 0:
                print(f'Вы ввели отрицательное дробное число: {string}')
            else:
                print(f'Вы ввели дробное число: {string}')
        else:
            print(f'Вы ввели отрицательное число: {string}')



