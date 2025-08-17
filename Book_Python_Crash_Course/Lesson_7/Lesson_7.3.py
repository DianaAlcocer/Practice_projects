sandwich_order = ['atun','pastrini','huevo','pastrini','jamon','nutella','pastrini']
sandwich_terminados = []

ingredients_missing = 'pastrini'

print(f'La tienda Delicatessen se ha quedado sin {ingredients_missing}')
while ingredients_missing in sandwich_order:
    sandwich_order.remove(ingredients_missing)


while sandwich_order:
    actual_order = sandwich_order.pop()
    print(f'Hice tu sandwich de {actual_order}')
    sandwich_terminados.append(actual_order)


print('Los siguientes sandwiches han sido preparados: ')
for sandwich in sandwich_terminados:
    print(sandwich)
