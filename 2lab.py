### программа для подбора банка и процентной ставки по вкладу ###

class Deposit:
    def __init__(self, bank, interest_rate, min_sum, max_sum, lasting):
        self.bank = bank
        self.interest_rate = interest_rate  #процентная ставка
        self.min_sum = min_sum              #минимальная сумма вклада
        self.max_sum = max_sum              #максим. сумма вклада
        self.lasting = lasting              #длительность вклада в месяцах

deposit1 = Deposit('Сбербанк', 0.06, 10000, 2000000, 24)
deposit2 = Deposit('Сбербанк', 0.07, 100000, 3000000, 12)
deposit3 = Deposit('Открытие', 0.07, 10000, 1000000, 24)
deposit4 = Deposit('ВТБ', 0.05, 1000, 2000000, 24)

print(deposit1.__dict__, deposit2.__dict__, deposit3.__dict__, deposit4.__dict__)

class Сlient:
    def __init__(self, name, deposit_amount, lasting):
        self.name = name                      #имя клиента
        self.deposit_amount = deposit_amount  #желаемая сумма вклада
        self.lasting = lasting                #желаемая длительность вклада в месяцах

print('Введите Ваше имя, желаемую сумма вклада, желаемую длительность вклада в месяцах:')

client = Сlient(name=input(), deposit_amount=input(), lasting=input())
