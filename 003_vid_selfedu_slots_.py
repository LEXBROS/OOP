class Point:
    WIDTH = 200

    __slots__ = ('x', 'y')  # РАЗРЕШЕННЫЕ АТРИБУТЫ

    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(5, 10)  # Setattr вызван при изменении атрибута
# Setattr вызван при изменении атрибута
p1.z = 10  # AttributeError: 'Point' object has no attribute 'z'
