class Hero:
    """Описание класса"""

    live = 'Like Hero!'
    damage = 0


print(getattr(Hero, 'live'))
print(Hero.live)

print(Hero.damage)
setattr(Hero, 'damage', 100)
print(getattr(Hero, 'damage'))

print(Hero.__dict__)  # магический метод выводящий все атрибуты класса
print(Hero.__doc__)

# print(Hero.attribute) тут будет ошибка AttributeError так как нет такого атрибута у класса Hero
