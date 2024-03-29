# Создайте класс Lion. В нем должен быть метод roar, который печатает на экран "Rrrrrrr!!!"

class Lion:

    def roar(self):
        print('Rrrrrrr!!!')

# Создайте класс Counter, экземпляры которого будут подсчитывать внутри себя значения.
# В классе Counter нужно определить метод start_from, который принимает один необязательный
# аргумент - значение, с которого начинается подсчет, по умолчанию равно 0
# Также нужно создать метод increment, который увеличивает счетчик на 1.
# Затем необходимо создать метод display, который печатает фразу
# "Текущее значение счетчика = <value>" и метод reset,  который обнуляет экземпляр счетчика
class Counter:

    def start_from(self, start=0):
        self.count = start

    def increment(self):
        self.count += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.count}')

    def reset(self):
        self.count = 0

c1 = Counter()
c1.start_from()
c1.increment()
c1.display()
c1.increment()
c1.display()
c1.reset()
c1.display()

c2 = Counter()
c2.start_from(3)
c2.display()
c2.increment()
c2.display()

# Создайте класс Point. У этого класса должны быть метод set_coordinates,
# который принимает координаты по x и по y, и сохраняет их в экземпляр класса
# соответственно в атрибуты x и y
# метод get_distance, который обязательно принимает экземпляр класса Point
# и возвращает расстояние между двумя точками по теореме Пифагора.
# В случае, если в данный метод передается не экземпляр класса Point
# необходимо вывести сообщение "Передана не точка"

class Point:

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, instancePoint):
        if isinstance(instancePoint, Point):
            return (((abs(self.x - instancePoint.x)) ** 2 + (abs(self.y - instancePoint.y)) ** 2) ** 0.5)
        else:
            print('Передана не точка')

p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2) # вернёт 5.0
p1.get_distance(10) # Распечатает "Передана не точка"
