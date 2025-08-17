# Declaración if - else

print('Alien Colors #1')

alien_color = 'rojo'

if alien_color == 'verde':
    print('Acabas de ganar 5 puntos')

print('Alien Colors #2')

if alien_color == 'verde':
    print('Acabas de ganar 5 puntos')
else:
    print('Acabas de ganar 10 puntos')

# Declaración if - elif - else

print('Alien Colors #3')

if alien_color == 'verde':
    print('Acabas de ganar 5 puntos')
elif alien_color == 'amarillo':
    print('Acabas de ganar 10 puntos')
elif alien_color == 'rojo':
    print('Acabas de ganar 15 puntos')

print('Etapas de la vida')

edad = 17

if edad < 2:
    print('Es un bebe')
elif edad >= 2 and edad < 4:
    print('Es un niño pequeño')
elif edad >= 4 and edad < 13:
    print('Es un niño')
elif edad >= 13 and edad < 20:
    print('Es un adolescente')
elif edad >= 20 and edad < 65:
    print('Es un adulto')
else:
    print('Es una persona mayor')

# Declaración if multiples

print('Fruta favorita')

fav_fruit = ['manzana', 'pera', 'uva']

if 'manzana' in fav_fruit:
    print('Realmente te gusta la manzana')
if 'fresa' in fav_fruit:
    print('Realmente te gusta la fresa')
if 'uva' in fav_fruit:
    print('Realmente te gusta la uva')
if 'naranja' in fav_fruit:
    print('Realmente te gusta la naranja')
if 'pera' in fav_fruit:
    print('Realmente te gusta la pera')
