fork1 = input()
fork2 = input()
fork3 = input()

if fork1 == 'vertebrado':
    if fork2 == 'ave':
        if fork3 == 'carnivoro':
            animal = 'aguia'
        elif fork3 == 'onivoro':
            animal = 'pomba'
    elif fork2 == 'mamifero':
        if fork3 == 'onivoro':
            animal = 'homem'
        elif fork3 == 'herbivoro':
            animal = 'vaca'
elif fork1 == 'invertebrado':
    if fork2 == 'inseto':
        if fork3 == 'hematofago':
            animal = 'pulga'
        elif fork3 == 'herbivoro':
            animal = 'lagarta'
    elif fork2 == 'anelideo':
        if fork3 == 'hematofago':
            animal = 'sanguessuga'
        elif fork3 == 'onivoro':
            animal = 'minhoca'

print(animal)