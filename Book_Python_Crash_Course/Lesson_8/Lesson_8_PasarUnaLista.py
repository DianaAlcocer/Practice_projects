def eleccion_de_ejercicio(op):

    if op == "8.9":

        # Ejercicio 8.9, mensajes (ERROR: El bucle no tiene fin)

        def show_message(msg_li):

            while msg_li:
                print(msg_li)

        msg_unprinted = ['hola 1', 'hola 2', 'hola 3']

        show_message(msg_unprinted)

    elif op == "8.10":

        # Ejercicio 8.10, send messages

        def send_message(send):
            while send:
                msg = send_msg.pop()
                print(msg)
                sent_msg.append(msg)

        send_msg = ["hola 1", "hola 2", "hola 3"]
        sent_msg = []

        send_message(send_msg)
        print(f'\nSend_msg list: {send_msg}')
        print(f'\nSent_msg list: {sent_msg}')

    elif op == "8.11":

        # Ejercicio 8.11, send messages copy

        def send_message(send):
            while send:
                msg = send.pop()
                print(msg)
                sent_msg.append(msg)

        send_msg = ["hola 1", "hola 2", "hola 3"]
        sent_msg = []

        send_message(send_msg[:])
        print(f'\nSend_msg list: {send_msg}')
        print(f'\nSent_msg list: {sent_msg}')

option = input ('¿Cual ejercicio deseas probar? ')
eleccion_de_ejercicio(option)