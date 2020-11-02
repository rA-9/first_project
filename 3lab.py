### программа для подбора банка и процентной ставки по вкладу ###

import csv

class Deposit:
    def __init__(self, bank, interest_rate, min_sum, max_sum, lasting):
        self.bank = bank
        self.interest_rate = interest_rate  #процентная ставка
        self.min_sum = min_sum              #минимальная сумма вклада
        self.max_sum = max_sum              #максим. сумма вклада
        self.lasting = lasting              #мин.длительность вклада в месяцах

deposit1 = Deposit('Сбербанк', '6%', 10000, 2000000, 12)
deposit2 = Deposit('Альфа', '7%', 100000, 3000000, 12)
deposit3 = Deposit('Открытие', '7%', 10000, 2000000, 24)
deposit4 = Deposit('ВТБ', '5%', 1000, 2000000, 24)

#print(deposit1.__dict__, deposit2.__dict__, deposit3.__dict__, deposit4.__dict__)

def read_csv():                                                        #метод вызова чтения файла
    with open('C:\\Users\\AAZhirova\\first_project\\1.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            print(row)
read_csv()

class Сlient:
    def __init__(self, name, deposit_amount, lasting):
        self.name = name                      #имя клиента
        self.deposit_amount = deposit_amount  #желаемая сумма вклада
        self.lasting = lasting                #желаемая длительность вклада в месяцах

    def change_lasting():                         #метод класса смена желаемой длительности вклада
        print('Введите другую длительность вклада в месяцах:')
        client.deposit_amount = int(input())


    def Writer_Client_csv():
        myData = [["name", "deposit_amount", "lasting"],
            [client.name, client.deposit_amount, client.lasting]]
        myFile = open('C:\\Users\\AAZhirova\\first_project\\2.csv', 'w')
        with myFile:
            writer = csv.writer(myFile, delimiter=';')
            writer.writerows(myData)
        print("Запись прошла успешно!")

print('Введите Ваше имя и фамилию, желаемую сумма вклада, желаемую длительность вклада в месяцах:')

client = Сlient(name=input(), deposit_amount=int(input()), lasting=int(input()))

Writer_Client_csv()

answer = 'y'

while answer != 'n':
    if (client.deposit_amount >= 1000 and client.deposit_amount <= 2000000 and client.lasting >= 24):
        print('Вам подходит вклад в банке Открытие, процентная ставка:', deposit3.interest_rate, 'и в банке банке ВТБ, процентная ставка:', deposit4.interest_rate)
    elif (client.deposit_amount >= 1000 and client.deposit_amount <= 10000 and client.lasting >= 24):
        print('Вам подходит вклад в банке ВТБ процентная ставка:', deposit4.interest_rate)
    elif (client.deposit_amount >= 100000 and client.deposit_amount <= 3000000 and client.lasting >= 12):
        print('Вам подходит вклад в банке Альфа, процентная ставка:', deposit2.interest_rate)
    elif (client.deposit_amount >= 10000 and client.deposit_amount <= 2000000 and client.lasting >= 12):
        print('Вам подходит вклад в банке Сбербанк, процентная ставка:', deposit1.interest_rate)
    else:
        print ('Подходящих банков не найдено')

    print('Желаете изменить длительность вклада? y/n')
    answer = input()
    if answer == 'y':
        change_lasting()        #вызов метода класса


    