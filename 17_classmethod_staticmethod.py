class Robot:
    __population = 0

    def __init__(self, name):
        self.name = name
        print(f'Робот {self.name} был создан')
        Robot.population_append()

    def destroy(self):
        print(f'Робот {self.name} был уничтожен')
        del self
        Robot.population_del()

    def say_hello(self):
        print(f'Робот {self.name} приветствует тебя, особь человеческого рода')

    @staticmethod
    def population_append():
        Robot.__population += 1

    @staticmethod
    def population_del():
        Robot.__population -= 1

    @classmethod
    def how_many(cls):
        print(f'{cls.__population}, вот сколько нас еще осталось')


r2 = Robot("R2-D2") # печатает "Робот R2-D2 был создан"
r2.say_hello() # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
Robot.how_many() # печатает "1, вот сколько нас еще осталось"
r2.destroy() # печатает "Робот R2-D2 был уничтожен"