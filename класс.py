from Verification import Verification


class V2(Verification):


    def __init__(self, login, password):
        super().__init__(login, password)
        self.__save()


    def __save(self):
        with open('users') as r:
            for i in r:
                if f'{self.login}'+'\n' == i:
                    raise ValueError ('Такой есть')
        super().save()



    def show(self):
        return self.login, self.password


x = V2('Bob', '3333333333')
"""
log = input('Введите логин: ')
pas = input('Введите пароль: ')
ag = input('Введите возраст: ')
x = V2(log, pas, ag)
"""


