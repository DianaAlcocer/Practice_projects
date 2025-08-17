ask = True
while ask !=  'salir':
    ask = input(f'¿Que ingrediente desea agregar? ')
    if ask != 'salir':
        print(f'Se agregara a su pizza')
    else:
        break