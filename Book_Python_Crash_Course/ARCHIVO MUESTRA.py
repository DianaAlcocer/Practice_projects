choice = True

while choice:

    def eleccion_de_ejercicio(op):

        if op == "8.9":
            print()

        elif op == "8.10":
            print()

    option = input ('¿Cual ejercicio deseas probar? ')
    eleccion_de_ejercicio(option)

    ask = input('\n¿Quieres probar otro ejercicio? S/N: ')

    if ask == "s" or ask == "S":
        choice = True
    elif ask == "n" or ask == "N":
        choice = False