#Ejercicio 8.3, Camiseta


def make_shirt(talla, mensaje):
    print(f"Es talla {talla}, el mensaje sera: {mensaje}")

#Argumento posicional

make_shirt("Grande","Es mi cumpleaños")

make_shirt("Es mi cumpleaños","Grande") #Error

#Argumento de palabra clave

make_shirt(talla="Grande", mensaje="Es tu cumple")

def make_shirt_g(talla="Grande", mensaje= "Me encanta python"):
    print(f"Es talla {talla}, el mensaje sera: {mensaje}")

#Ejercicio 8.4, Usando predeterminados

make_shirt_g()

make_shirt_g(talla="Mediana") #especificando solo 1 argumento con clave, y 1 predeterminado

make_shirt_g("Mediana2") # especificando solo 1 argumento sin clave, y 1 predeterminado

make_shirt_g(mensaje="Me gusta C++",talla="Pequeña") # especificando ambos argumentos con clave en desorden

make_shirt_g("ExtraPequeña","Me gusta Java") # especificando ambos argumentos posicionales

#Ejercicio 8.5, ciudades

def describe_city(city, country="china"):
    print(f'{city} esta en {country}')

describe_city("monterrey")

describe_city("monterrey", "mexico")