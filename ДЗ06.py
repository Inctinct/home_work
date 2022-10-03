import json
import csv


def create_json():
    data =[
    {
        "name": "John Smith",
        "birthday": "02.10.1990",
        "height": 175,
        "weight": 76.5,
        "car": True,
        "languages": ["C++", "Python"]
    },


    {
        "name": "Alexey Alexeev",
        "birthday": "05.06.1986",
        "height": 197,
        "weight": 101.2,
        "car": False,
        "languages": ["Pascal", "Delphi"]
    },
    {
        "name": "Maria Ivanova",
        "birthday": "28.08.1998",
        "height": 165,
        "weight": 56.1,
        "car": True,
        "languages": ["C#", "C++", "C"]
    }
]
    with open('data_file.json','w') as f:
        json.dump(data,f)

def add_to_json():
    name = input('Set a name: ')
    birthday=input('Set a birthday: ')
    height=input('Set a height: ')
    weight=input('Set a weight: ')
    car=input('Have a car? True/False: ')
    languages=list(input('Set languages: ').split())
    json_data={

        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car,
        "languages":languages
    }
    data=json.load(open('data_file.json'))
    data.append(json_data)
    with open("data_file.json", "w") as f:
        json.dump(data,f)



def json_to_csv():
    with open('data_file.json', 'r') as f:
        data = json.loads(f.read())
    cols = ['name', 'birthday', 'height', 'weight', 'car', 'languages']
    with open('some.csv', 'w', newline='') as f:
        wr = csv.DictWriter(f, fieldnames=cols)
        wr.writeheader()
        wr.writerows(data)
def csv_to_json():
    data = []
    count = 0
    with open('some.csv', encoding='utf-8') as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            if count !=0:
                data.append(row)
            count+=1
    with open('data_file.json', 'w', encoding='utf-8') as f:
        json.dump(data,f)



def add_to_csv():
    name = input('Set a name: ')
    birthday = input('Set a birthday: ')
    height = input('Set a height: ')
    weight = input('Set a weight: ')
    car = input('Have a car? True/False: ')
    languages = list(input('Set languages: ').split())
    arr=[]
    csv_data= {

        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car,
        "languages": languages

    }
    for key,value in csv_data.items():
        arr.append(value)
    cols = ['name', 'birthday', 'height', 'weight', 'car', 'languages']
    with open('some.csv','a',newline='') as f:
        wr = csv.writer(f)
        wr.writerow(arr)

def inf_name_json():
    data = json.load(open('data_file.json'))
    name=input('Set a name: ')
    for i in data:
        for key,value in i.items():
            if value == name:
                print(i)

def inf_lang_json():
    data = json.load(open('data_file.json'))
    lang=input('Set a language: ')
    for i in data:
        for j in i.get('languages'):
            if j == lang:
                print(i.get('name'))

def inf_height_json():
    age = []
    summa = 0
    count = 0
    data = json.load(open('data_file.json'))
    birthday = input('Set a year: ')
    for i in data:
        age.append(i.get('birthday').split('.'))
        if age[0][2] < birthday:
            summa+=int(i.get('height'))
            count+=1
        age.clear()
    print(f'average height = {summa/count}')


def inf_name_csv():
    name = input('Set a name:')
    with open("some.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file)
        for row in file_reader:
            if row[0] == name:
                print(row)

def inf_lang_csv():
    lang = input('Set a language: ')
    count=0
    arr=[]

    with open("some.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file)
        for row in file_reader:
            if count != 0:
                for j in row[5].split("'"):
                   if j == lang:
                        print(row[0])
            count+=1


def inf_height_csv():
    cou=0
    summa=0
    count=0
    birthday = input('Set a year: ')
    with open("some.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file)
        for row in file_reader:
            if count !=0:
                if row[1][6:10]<birthday:
                    summa+=int(row[2])
                    cou+=1
            count+=1
        print(f'average height = {summa/cou}')




"""
При Первом запуске включить две функции, чтобы в json и csv файлы залились данные людей из условия задачи
"""

#create_json()
#json_to_csv()







action = 0
while action !=1:
    choice = int(input('1.Add informatin\n2.Serch by name\n3.Serch by language\n4.average height by age\n5.Exit'))
    if choice==5:
        exit(0)
    option = int(input('1.Jsoin\n2.CSV'))

    if option == 1:
        if choice ==1:
            add_to_json()
            json_to_csv()
        if choice == 2:
            inf_name_json()
        if choice == 3:
            inf_lang_json()
        if choice == 4:
            inf_height_json()

    if option == 2:
        if choice ==1:
            add_to_csv()
            csv_to_json()
        if choice == 2:
            inf_name_csv()
        if choice == 3:
            inf_lang_csv()
        if choice == 4:
            inf_height_csv()



