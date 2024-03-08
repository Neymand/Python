from collections import defaultdict
class Product:
    #__balance = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price

class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f"Пользователь {self.login}, баланс - {self.balance}"

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_bal):
        self.__balance = new_bal

    def deposit(self, val):
        if isinstance(val, int):
            self.__balance += val

    def is_money_enough(self, val):
        if isinstance(val, int):
            return val <= self.__balance

    def payment(self, val):
        if self.is_money_enough(val):
            self.__balance -= val
            return True
        else:
            print('Не хватает средств на балансе. Пополните счет')

class Cart:
    def __init__(self, user):
        if isinstance(user, User):
            self.user = user
            self.goods = defaultdict()
            self.__total = 0

    def add(self, product, col=1):
        self.goods[product] = self.goods.get(product, 0) + col    # Прибавление к уже существующему значению.
        self.__total += product.price * col

    def remove(self, product, col=1):     # Правильная реализация
        if isinstance(product, Product):
            min_n = min(col, self.goods[product])
            self.goods[product] -= min_n
            self.__total -= min_n*product.price
            if not self.goods[product]:
                del self.goods[product]
    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.__total):
            print('Заказ оплачен')
        else:
            print('Проблема с оплатой')

    def print_check(self):
        print('---Your check---')
        for key, val in sorted(self.goods.items(), key=lambda x: x[0].name):
            print(f'{key.name} {key.price} {val} {val*key.price}')
        print(f'---Total: {self.total}---')











