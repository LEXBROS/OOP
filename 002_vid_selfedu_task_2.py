# Объявите класс Point с конструктором, который бы позволял создавать
# экземпляр на основе уже существующего экземпляра. Если аргументы в
# конструктор не передаются, то создается объект с локальными атрибутами по умолчанию.

class Point:
    def __init__(self, instance=None, x=0, y=0):
        if instance is None:
            self.x = x
            self.y = y
        else:
            self.x = instance.x
            self.y = instance.y


p_1 = Point()
print(p_1.__dict__)
p_1.x = 11
p_1.y = 12
p_2 = Point(p_1)
print(p_2.__dict__)
