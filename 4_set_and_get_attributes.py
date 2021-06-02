class Hero:
    live = 'Like Hero!'
    damage = 0


print(getattr(Hero, 'live'))
print(Hero.live)

print(Hero.damage)
setattr(Hero, 'damage', 100)
print(getattr(Hero, 'damage'))

print(Hero.attribute)
