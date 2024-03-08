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


# Nds = Product('Nintendo ds', 5000)
# lemon = Product('Lemon', 55)
# guitar = Product('Epiphone classic', 16000)
# laptop = Product('Huawey mate book', 40000)
# apple = Product('Apple', 15)
#
# kirill = User('kirilll', 6000)
#
# py = Cart(kirill)
#
# py.add(Nds)
# py.add(guitar, 3)
# py.add(laptop)
# py.add(apple, 5)
# py.add(lemon)
#
# py.order()
# py.print_check()

billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20








