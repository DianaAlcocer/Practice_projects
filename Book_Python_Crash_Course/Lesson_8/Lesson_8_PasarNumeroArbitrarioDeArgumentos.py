choice = True

while choice:

    def eleccion_de_ejercicio(op):

        if op == "e1":

            # Ejemplo1. EL arterisco le indica a la funcion que tome los argumentos como una tupla

            def make_pizza(*ingredientes):
                print(ingredientes)

            make_pizza('piña')
            make_pizza('champiñones','extra queso','aceituna')

        elif op == "e2":

            # Ejemplo2. La funcion anidada 'for', hace que tome individual cada elemento de la tupla

            def make_pizza(*ingredientes):
                print('Preparando una pizza con los siguientes ingredientes: ')
                for topping in ingredientes:
                    print(topping)


            make_pizza('piña')
            make_pizza('champiñones', 'extra queso', 'aceituna')

        elif op == "e3":

            # Ejemplo3. La función primero toma parámetros posicionales o por clave y
            #           los argumentos restantes se agrupan en una tupla en el último parametro.

            def make_pizza(size, *ingredientes):
                print(f'Preparando una pizza de {size} con los siguientes ingredientes: ')
                for topping in ingredientes:
                    print(topping)

            make_pizza(16,'piña')
            make_pizza(12,'champiñones', 'extra queso', 'aceituna')

        elif op == "e4":

            #Ejemplo4. Un * es tupla. Dos ** es diccionario.

            def build_profile(first_name, last_name, **user_info):

                user_info['firstName'] = first_name
                user_info['lastName'] = last_name
                return user_info

            user_profile = build_profile('Albert','Einstein',locaton='Princeton',subject='fisica')
            print(user_profile)

        elif op == "8.12":

            #Ejercicio 8.12.

            def make_sandwich(*ingredients):
                for item in ingredients:
                    print(item)

            make_sandwich('jamon','queso','lechuga','tomate','aguacate')

        elif op == "8.13":

            # Ejercicio 8.13. Perfil de usuario

            def build_profile(first,last,**info):
                info['first']=first
                info['last']=last
                return info

            user_profile = build_profile('Diana','Alcocer',EstadoCivil='Casada',Hijos='2',Profesion='QA Tester')
            print(user_profile)

        elif op == "8.14":

            # Ejercicio 8.14. Automoviles

            def build_car_info(name,model,**info):
                info['manufactur'] = name
                info['model_car'] = model
                return info

            car_info = build_car_info('subaru','x2',color='blue',tow_package=True)
            print(car_info)



    option = input('\n¿Cual ejercicio deseas probar? ')
    eleccion_de_ejercicio(option)

    ask = input('\n¿Quieres probar otro ejercicio? S/N: ')

    if ask == "s" or ask == "S":
        choice = True
    elif ask == "n" or ask == "N":
        choice = False