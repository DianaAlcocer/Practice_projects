print('\nCASO 1: Incluyendo y modificando valores en un diccionario.\n')

alien_1 = {}

alien_1['color'] = 'verde'
alien_1['puntos'] = '5'

print(alien_1)
print(f'\nEl alien es color {alien_1["color"]}')

alien_1['color'] = 'amarillo'

print(f'\nEl alien ahora es color {alien_1["color"]}')

print('\nCASO 2: Modificando valores en un diccionario con el uso de if.\n')

alien_2 = {'x_position': 0, 'y_position': 25, 'velocidad': 'media'}

print(f'Posición horizontal original: {alien_2["x_position"]}')

if alien_2['velocidad'] == 'lenta':
    incremento_x = 1
elif alien_2['velocidad'] == 'media':
    incremento_x = 2
else:
    incremento_x = 3

alien_2['x_position'] = alien_2['x_position'] + incremento_x

print(f'Posición horizontal actual: {alien_2["x_position"]}')

print('\nCASO 3: Borrando una clave que ya no se utiliza.\n')

print(alien_1)

del alien_1['puntos']

print(alien_1)

print("\nCASO 4: Obteniendo una clave que podría no estar, sustituye diccionario['clave'].\n")

alien_puntos = alien_1.get('puntos', 'No existe esa clave en el diccionario')
print(alien_puntos)

print("\nCASO 5: Obteniendo información de un diccionario].\n")

for c, valor in alien_2.items():
    print(f'{c} = {valor}.')

for name in alien_2.keys():
    print(name.title())

print("\nCASO 6: Obteniendo información especifica de un diccionario].\n")

amigos = ['phil', 'sara']
idiomas = {
    'jen': 'python',
    'sara': 'c',
    'eduard': 'java',
    'phil': 'python'
    }

for name in sorted(idiomas.keys()):  # la función sorted devuelve las claves en orden, y key devuelve las claves
    print(f'\tHola {name.title()}.')
    
    if name in amigos:
        idioma = idiomas[name].title()
        print(f'\t\t{name.title()}, ¡Veo que te encanta {idiomas[name].title()}!')

for idioma in set(idiomas.values()):  # la función set devuelve valores no repetidos, y values devuelve los valores
    print(idioma.title())
