from random import randint

health = 100
destiny = randint(1,99)
if destiny < 34:
    name = 'Garik'
elif destiny < 67:
    name = 'Soldatov'
else:
    name = 'Nikita'

if health - randint(30, 130) < 0:
    print(name + ' pidor')
else:
    print(name + ' gey')
