class Car:
    model = 'VAZ'  # атрибуты класса
    color = 'Black'  # атрибуты класса


first_car = Car()
second_car = Car()

print(first_car.model)  # VAZ
print(second_car.model)  # VAZ

Car.model = 'BMW'  # меняем модель в пространстве имен самого класса

print(first_car.model)  # BMW
print(second_car.model)  # BMW

first_car.model = 'DODGE'  # добавляем атрибут в пространство имен конкретного экземпляра

print(first_car.model)  # DODGE
print(second_car.model)  # BMW

Car.model = 'FORD'

print(first_car.model)  # DODGE экземпляр класса нашел значение в своем собственном пространстве имен
print(second_car.model)  # FORD экземпляр класса не нашел значение в своем собственном пространстве имен и поднялся на
# уровень выше и нашел его в пространстве имен класса
