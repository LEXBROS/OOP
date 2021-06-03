# Создайте класс Point3D, который хранит координаты в виде списка.
# Пропишите у него конструктор для создания экземпляров с локальными
# координатами. Также добавьте методы, позволяющие изменять координаты и
# получать их (в виде кортежа).

class Point3D:
    coords = []

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        Point3D.coords.append(self.__dict__)

    def set_coords(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coords(self):
        return self.x, self.y, self.z


p_1 = Point3D(0, 0, 0)
print(Point3D.coords)
p_1.set_coords(1, 2, 3)
print(Point3D.coords)
print(p_1.get_coords())
p_2 = Point3D(8, 8, 8)
print(Point3D.coords)
p_1.set_coords(9, 9, 9)
print(Point3D.coords)
