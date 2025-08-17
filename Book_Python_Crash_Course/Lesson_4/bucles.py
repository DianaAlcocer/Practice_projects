lista_de_magos = ['alicia', 'david', 'carolina']

for name in lista_de_magos:
    print(f'Bien hecho {name.title()}')
    
for valor in range(1, 5):  # El segundo valor no se imprime
    print(valor)

lista = list(range(1, 6))  # Convertir un rango en lista
print(lista)

lista2 = list(range(1, 6, 2))  # Crear una lista saltando dos números
print(lista2)

# Agregar elementos a una lista usando un bucle
cuadrados = []  # lista vacía
for valor in range(1, 11):
    cuadrados.append(valor**2)
print(cuadrados)

# Lista de comprensión
cuadrados = [valor**2 for valor in range(1, 11)]
print(cuadrados)

# Encontrar el minimo, máximo y suma de una lista de números
edades = [2, 5, 6, 3, 9, 10]
print(min(edades))
print(max(edades))
print(sum(edades))
