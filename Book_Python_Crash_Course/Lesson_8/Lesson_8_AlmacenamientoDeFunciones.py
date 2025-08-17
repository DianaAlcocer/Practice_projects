

choice = True

while choice:


    def eleccion_de_ejercicio(op):

        if op == "e1":

        # Importar un modulo

            import pizza

            pizza.make_pizza(16, 'piña')
            pizza.make_pizza(12, 'champiñones', 'extra queso', 'aceituna')

        elif op == "e2":

        # Importar una funcion especifico de un modulo, se pueden agregar mas separadas por coma.

            from pizza import make_pizza

            make_pizza(16, 'piña')
            make_pizza(12, 'champiñones', 'extra queso', 'aceituna')

        elif op == "e3":

            # Importar una funcion especifica de un modulo usando un alias

            from pizza import make_pizza as mp

            mp(16, 'piña')
            mp(12, 'champiñones', 'extra queso', 'aceituna')

        elif op == "e4":

            # Importar un modulo usando un alias

            import pizza as p

            p.make_pizza(16, 'piña')
            p.make_pizza(12, 'champiñones', 'extra queso', 'aceituna')

        elif op == "e5":

            # Importar un modulo usando arterisco para traer todas sus funciones.
            #Se utiliza solo al inicio del modulo.

            from pizza import *

            make_pizza(16, 'piña')
            make_pizza(12, 'champiñones', 'extra queso', 'aceituna')

    option = input ('¿Cual ejercicio deseas probar? ')
    eleccion_de_ejercicio(option)

    ask = input('\n¿Quieres probar otro ejercicio? S/N: ')

    if ask == "s" or ask == "S":
        choice = True
    elif ask == "n" or ask == "N":
        choice = False