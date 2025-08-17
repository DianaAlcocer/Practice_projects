lista = ['carne', 'leche', 'harina', 'huevo']
print(f'Mi bebida favorita es la {lista[1].upper()}')

# Modificar elementos de una lista
print(lista)
lista[2] = 'harina de trigo'
print(lista)

# Agregar elementos
lista.append('frijol')
lista.insert(1, 'pescado')
print(lista)

# Eliminar elementos
lista1 = 'leche'
lista.remove(lista1) 
"""la función remove se puede utilizar sola para eliminar un valor,
Pero solo elimina la primera aparición de ese valor, si se quiere eliminar todas, hay que usar un bucle.
Y si se quiere utilizar ese valor removido, primero se declara una variable 
y luego se remueve el valor de esa variable."""
lista2 = lista.pop(3)
lista3 = lista.pop()
print(lista)
print(lista1)
print(lista2)
print(lista3)

# Copiar una lista
lista5 = lista.copy()
lista6 = lista.copy()
print(f'Copia de la lista: {lista5}')

# Organizar elementos
print(f'Lista original:{lista5}')
print(f'Lista ordenada temporalmente: {sorted(lista5)}')  # Ordena temporalmente
print(f'Lista ordenada temporalmente al inverso: {sorted(lista5,reverse=True)}')  # Ordena temporalmente
print(f'Lista original nuevamente: {lista5}')

lista5.sort()  # ordena alfabéticamente y permanentemente
print(f'Lista ordenada permanentemente: {lista5}')
lista5.sort(reverse=True)  # Ordena alfabéticamente inverso
print(f'Lista ordenada al revés: {lista5}')
lista6.reverse()  # ordena la lista al inverso, no alfabéticamente inverso
print(f'Lista original ordenada al revés: {lista6}')

# Longitud de una lista
print(len(lista6))

# La lista usa [], la tupla usa (), el diccionario usa {}
lista = ['a', 'b', 'c']
tupla = (1, 2, 3)
diccionario = {
    'nombre': 'diana',
    'apellido': 'alcocer',
    'teléfono': 811498
    }
