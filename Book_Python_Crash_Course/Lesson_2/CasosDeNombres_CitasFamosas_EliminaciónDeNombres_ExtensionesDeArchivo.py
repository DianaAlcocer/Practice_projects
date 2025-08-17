name = "ada lovelace"
print(f'Ejemplo de función title directo en la funcion print: {name.title()}')

print(f'La variable no cambia en realidad: {name}')

name = name.upper()

print(f'Modificando la variable con la función upper: {name}')

name = name.lower()

print(f'Modificando la variable con la función lower: {name}')

name = name.title()

print(f'Modificando la variable con la función title: {name}')

frase1 = 'Agregar: \nSaltos de linea y \ttabulaciones.'
print(frase1)

frase3 = ' Espacios al inicio y al final '
print(f'Eliminar espacios al final: \n->{frase3.rstrip()}.<-')
print(f'Eliminar espacios al inicio: \n->{frase3.lstrip()}.<-')
print(f'Eliminar espacios a ambos lados: \n->{frase3.strip()}.<-')

frase4 = 'https://wikipedia.com'
print(frase4)
print(f'Eliminando prefijos: {frase4.removeprefix("https://")}')

frase5 = 'mi_archivo.txt'
print(frase5)
print (f'Eliminando sufijos: {frase5.removesuffix(".txt")}')