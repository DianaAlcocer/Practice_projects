pizzas_favoritas = ['champiñones', 'hawaiana', '3 carnes']
for pizza in pizzas_favoritas:
    print(f'Me gusta la pizza de {pizza}.')

print('Podría comer pizza todos los dias')

pizzas_favoritas.append('pepperoni')
pizzas_favoritas.append('vegetariana')
pizzas_favoritas.append('mexicana')

print(f'Los primeros 3 elementos son: {pizzas_favoritas[:3]}')
print(f'3 elementos de enmedio son: {pizzas_favoritas[2:5]}')
print(f'Los últimos 3 elementos de la lista son {pizzas_favoritas[-3:]}')

friend_pizzas = pizzas_favoritas[:]

pizzas_favoritas.append('veggies')
friend_pizzas.append('supreme')

print(f'Mis pizzas favoritas son:')
for pizza in pizzas_favoritas:
    print(pizza)
print(f'Las pizzas favoritas de mi amigos son:')
for pizza in friend_pizzas:
    print(pizza)
