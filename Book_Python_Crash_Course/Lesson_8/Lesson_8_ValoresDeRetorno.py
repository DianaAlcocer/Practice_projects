
def eleccion_de_ejercicio(op):

    if op == "8.6":

        # Ejercicio 8.6, nombres de ciudades

        def get_city_country(city, country):
            lugar = f'{city }, {country}'
            return lugar.title()

        while True:
            print("\nIngrese una ciudad y pais")
            print("Ingrese S para salir")
            city = input("Ciudad: ")
            if city == "S":
                break
            country = input("Pais: ")
            if country == "S":
                break
        city_country = get_city_country(city, country)
        print(f'"{city_country}"')

    elif op == "8.7":

        # Ejercicio 8.7, album

        def make_album(artista,titulo,numero_canciones=None):
            album = {"artist": artista, "title": titulo}
            if numero_canciones:
                album["numero_canciones"] = numero_canciones

            return album

        while True:
            print("\nIngrese un artista y titulo del album")
            print("Ingrese S para salir")

            name_artista = input("Nombre artista: ")
            if name_artista == "S":
                break
            name_titulo = input("Nombre titulo: ")
            if name_titulo == "S":
                break
            num_canciones = input("Nombre titulo: ")
            if name_titulo == "S":
                break

            dic_album = make_album(artista=name_artista, titulo=name_titulo, numero_canciones=num_canciones)
            print(dic_album)

option = input ('¿Cual ejercicio deseas probar? ')
eleccion_de_ejercicio(option)







