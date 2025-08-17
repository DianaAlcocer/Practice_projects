"""
Los nombres de variables son sensibles
a mayúsculas y minúsculas,
son variables distintas.
Las comillas triples se utilizan para comentarios
de multiples líneas.
"""

_cars = 23  # Inicia con guion bajo
cars = 24   # Inicia con minúscula
CARS = 25   # Inicia con mayúscula

CARS = 254  # Se repite variable, reemplazando la anterior


# Tipos de variables

number_of_cars = 23         # Numerica
kind_of_cars = "Ferrari"    # Cadena con doble comilla
kind_of_cars_2 = 'Porche'   # Cadena con comilla simple

print(cars)
print(_cars)
print(CARS)
print(number_of_cars)
print(kind_of_cars)
print(kind_of_cars_2)

'''
Sumar cadenas, las une, no las modifica
Sumar números, se realiza la operacion
'''

print("Type of cars: " + kind_of_cars + ", " + kind_of_cars_2)
print("Type of cars: {}, {}".format(kind_of_cars, kind_of_cars_2))

print("Number of cars: ", _cars + cars)


def name():
    print("Hello world")


name()
