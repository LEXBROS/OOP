class Point:
    WIDTH = 200  # далее с помощью перегрузки метода setattr мы запретим ее изменять

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # далее следуют перегруженные функции, которые автоматически вызываются при наступлении
    # какого либо события (понятно по названию методов)

    def __setattr__(self, key, value):
        if key == 'WIDTH':
            raise AttributeError
        else:
            self.__dict__[key] = value

    def __getattribute__(self, item):  # ПЕРЕГРУЗКА ФУНКЦИИ
        if item == 'x':
            return 'Частная переменная'
        else:
            return object.__getattribute__(self, item)

    # def __getattr__(self, item):
    #     print('getattr вызван при обращении к несуществующему атрибуту')


p1 = Point(5, 10)  # Setattr вызван при изменении атрибута
# Setattr вызван при изменении атрибута
print(p1.x)  # Частная переменная
print(p1.y)  # 10
p1.WIDTH = 10  # AttributeError
