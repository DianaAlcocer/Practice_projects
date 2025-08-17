

prompt = "¿Buscas un coche de alquiler? "
prompt += "¿Que tipo de coche te gustaria?"

coche = input(f'{prompt}: ' )

print(f'Dejame ver si puedo encontrarte un {coche}.')


prompt = '\n\n¿Para cuantas personas sera la reserva? '

reserva = input(f'{prompt}')
reserva = int(reserva)

if reserva > 8:
    print(f'Tendrán que esperar por una mesa')
else:
    print('La mesa esta lista')

prompt = '\n\nDime un numero y te dire si es multiplo de 10: '

numero = input(f'{prompt} ')
numero = int(numero)

if numero % 10 == 0:
    print(f'{numero} es multiplo de 10')
else:
    print(f'{numero} NO es multiplo de 10')


