class Dog:

    # при таком определении функции мы можем вызвать ее только через экземпляр
    def say_vaf(self):
        print('Vaaaaffff!!!')


my_dog = Dog()

# Dog.say_vaf()  тут будет ошибка
my_dog.say_vaf()  # тут нормально


class Cat:

    # а при таком определении функции мы можем вызвать ее только через сам класс
    def say_may():  # старайся так не делать
        print('Meouuuu!!!')


my_cat = Cat()

Cat.say_may()  # тут нормально
# my_cat.say_may()  # а тут ошибка
