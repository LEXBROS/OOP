# Напишите программу, в которой пользователь вводит с клавиатуры координаты x, y.
# Создается соответствующий экземпляр и он сохраняется в списке. Количество вводимых объектов N=5.
# Затем необходимо вывести их атрибуты в консоль

class Point:
    instance_list = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.instance_list.append(self)


for i in range(int(input('Введите количество точек координат: '))):
    coord_x, coord_y = map(int, input('Введите 2 координаты через пробел и Enter: ').split())
    Point(coord_x, coord_y)

for j in Point.instance_list:
    print(j.__dict__)
