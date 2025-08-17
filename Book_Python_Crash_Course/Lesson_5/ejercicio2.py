# Prueba de booleanos

# Probando igualdad y desigualdad (==, !=)

coche = 'jeep'
print(f'¿coche == jeep? Predigo que sera verdadero')
print(coche == 'jeep')

print(f'¿coche != jeep? Predigo que sera falso')
print(coche != 'jeep')

# Probando mayúsculas y minúsculas (.lower, .upper, .title)

print(f'¿coche == Jeep? Predigo que sera falso porque es mayúscula')
print(coche == 'Jeep')

print(f'¿coche.title() == Jeep? Predigo que sera verdadero porque estoy modificando el case de la variable')
print(coche.title() == 'Jeep')

# Probando si un elemento esta o no está en una lista (in, not in)

request_toppings = ['champiñones', 'cebollas', 'piña']

print('Esta es la lista de toppings solicitados:')
print(request_toppings)

print('¿Esta la piña incluida?')
print('piña' in request_toppings)
print('¿Están los champiñones NO incluidos?')
print('champiñones' not in request_toppings)
print('¿Esta el pepperoni incluido?')
print('pepperoni' in request_toppings)

# Probando palabra clave and y or

print('Chequemos si se puede hacer la pizza con dos ingredientes')
print('Quiero la pizza con champiñones Y piña')
print('champiñones' in request_toppings and 'piña' in request_toppings)
print('Quiero la pizza con carne Y piña')
print('carne' in request_toppings and 'piña' in request_toppings)
print('Esta bien, puede ser con carne O piña')
print('carne' in request_toppings or 'piña' in request_toppings)

# Probando igualdades numéricas (<, <=, >=, >)

pizzas_solicitadas = 2

print('¿Cuantas pizzas solicitaron?')
print('Menos de 2?', pizzas_solicitadas < 2)
print('Mas de 2?', pizzas_solicitadas > 2)
print('O solo 2?', pizzas_solicitadas >= 2)
