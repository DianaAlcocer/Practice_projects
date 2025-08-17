print('CASO 1: No solicito ingredientes en su pizza')

request_ingredients = []

if request_ingredients:
    for ingredient in request_ingredients:
        print('Agregando {ingredient}')

    print('Tu pizza esta lista')

else:
    print('¿Seguro que quieres una pizza simple?')

print('CASO 2: Solicito pepperoni en su pizza')

request_ingredients.append('pepperoni')

if request_ingredients:
    for ingredient in request_ingredients:
        print(f'Agregando {ingredient}')

    print('Tu pizza esta lista')

else:
    print('¿Seguro que quieres una pizza simple?')

print('CASO 3: Solicito papas fritas en su pizza')

request_ingredients.append('papas fritas')

if request_ingredients:
    for ingredient in request_ingredients:
        print(f'Agregando {ingredient}')

    print('Tu pizza esta lista')

else:
    print('¿Seguro que quieres una pizza simple?')

print(
    '\n\nCASO 4: Solicito champiñones, papas fritas y queso extra. \n\tPero las papas fritas son un extra, no un topping')

available_ingredients = ['champiñones', 'aceitunas', 'pimientos verdes', 'pepperoni', 'piña', 'queso extra']
request_ingredients_2 = ['champiñones', 'papas fritas', 'queso extra']

for ingredient in request_ingredients_2:
    if ingredient in available_ingredients:
        print(f'Agregando {ingredient}')
    else:
        print(f'Lo sentimos, no tenemos {ingredient}')
print('\nTu pizza esta lista')

print('\n\nCASO 5')

usuarios = ['admin', 'vale', 'diana', 'vinc', 'ari']

for usuario in usuarios:
    if usuario == 'admin':
        print('Hola admin, ¿le gustaría ver el informe?')
    else:
        print(f'Hola {usuario}, bienvenido')

usuarios = []

if usuarios:
    print('Bienvenido')
else:
    print('Necesitamos encontrar algunos usuarios')

print('\n\nCASO 6')

usuarios_actuales = ['vale', 'DIANA']
usuarios_actuales_lower = [usuario.lower() for usuario in usuarios_actuales]
usuarios_nuevos = ['vinc', 'diana', 'ari']

for usuario in usuarios_nuevos:
    if usuario.lower() in usuarios_actuales_lower:
        print(f'El nombre de usuario {usuario} ya existe,'
              '\n por favor ingrese un nombre nuevo.')
    else:
        print(f'El nombre de usuario {usuario} esta disponible.')
