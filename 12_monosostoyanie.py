class Mono:
    __shared_attr = {'Name': 'Vasya',  # атрибут класса, на который в дальнейшем будут ссылаться все экземпляры
                     'age': 19}

    def __init__(self):
        self.__dict__ = Mono.__shared_attr  # здесь словарю атрибутов экземпляра
        # прикрепляется ссылка на общий атрибут для всех экземпляров класса


p1 = Mono()
p2 = Mono()
p1.Name = 'George'
print(p1.__dict__)
print(p2.__dict__)

# {'Name': 'George', 'age': 19}
# {'Name': 'George', 'age': 19}
