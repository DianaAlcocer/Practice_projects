usuarios_no_confirmados = ['a','b','c']
usuarios_confirmados = []

while usuarios_no_confirmados:
    usuario_actual = usuarios_no_confirmados.pop()
    print(f'Verificando usuario: {usuario_actual.title()}')
    usuarios_confirmados.append(usuario_actual)
print(f'Los siguientes usuarios han sido confirmados: ')
for usuario_confirmado in usuarios_confirmados:
    print(usuario_confirmado.title())