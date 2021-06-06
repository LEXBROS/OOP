class BankAccount:

    def __init__(self, name, balance, passport):  # публичные методы и атрибуты
        self.name = name  # публичные методы и атрибуты
        self.balance = balance  # публичные методы и атрибуты
        self.passport = passport  # публичные методы и атрибуты

    def print_data(self):  # публичные методы и атрибуты
        print(self.name, self.balance, self.passport)  # публичные методы и атрибуты


account1 = BankAccount('BOB', 305465, 4856256578)  # можем обращаться к методам и атрибутам извне
account1.print_data()  # можем обращаться к методам и атрибутам извне
print(account1.name)  # можем обращаться к методам и атрибутам извне
print(account1.balance)  # можем обращаться к методам и атрибутам извне
print(account1.passport)  # можем обращаться к методам и атрибутам извне


# BOB 305465 4856256578
# BOB
# 305465
# 4856256578

class BankAccount1:

    def __init__(self, name, balance, passport):  # методы и атрибуты protected
        self._name = name  # методы и атрибуты protected
        self._balance = balance  # методы и атрибуты protected
        self._passport = passport  # методы и атрибуты protected

    def _print_data(self):  # методы и атрибуты protected
        print(self._name, self._balance, self._passport)  # методы и атрибуты protected


account2 = BankAccount1('BOB', 305465, 4856256578)  # можем обращаться к методам и атрибутам извне
account2._print_data()  # можем обращаться к методам и атрибутам извне
print(account2._name)  # можем обращаться к методам и атрибутам извне
print(account2._balance)  # можем обращаться к методам и атрибутам извне
print(account2._passport)  # можем обращаться к методам и атрибутам извне


# BOB 305465 4856256578
# BOB
# 305465
# 4856256578

class BankAccount2:

    def __init__(self, name, balance, passport):  # методы и атрибуты private
        self.__name = name  # методы и атрибуты private
        self.__balance = balance  # методы и атрибуты private
        self.__passport = passport  # методы и атрибуты private

    def _print_data(self):  # методы и атрибуты private
        print(self.__name, self.__balance, self.__passport)  # методы и атрибуты private


account3 = BankAccount2('BOB', 305465, 4856256578)  # можем обращаться к методам и атрибутам извне
# account3.__print_data()  # не можем обращаться к методам и атрибутам извне
# print(account3.__name)  # не можем обращаться к методам и атрибутам извне
# print(account3.__balance)  # не можем обращаться к методам и атрибутам извне
# print(account3.__passport)  # не можем обращаться к методам и атрибутам извне

# но все таки можем вот так:
print(dir(account3))  # это чтобы подсмотреть как правильно написать атрибут
print(account3._BankAccount2__name)  # это чтобы вывести атрибут

# Traceback (most recent call last):
#   File "/home/lexbros/PycharmProjects/OOP/13_public_private_protected.py", line 58, in <module>
#     account3.__print_data()  # не можем обращаться к методам и атрибутам извне
# AttributeError: 'BankAccount2' object has no attribute '__print_data'
