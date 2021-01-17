def contador(lista):
    for palabra in lista:
        numero_de_palabras = len(palabra)
        print(f'La palabra {palabra} tiene {numero_de_palabras} palabras.')


def desicion(lista):
    eleccion = ''
    eleccion = input('Escribe contador si quieres ver el numero de letras en cada palabra, de lo contrario escribe no: ')
    if eleccion == 'contador':
        contador(lista)
    elif eleccion == 'no':
        print('Hasta la proxima')
    else:
        print('Escribiste mal la indicacion')


def inicio():
    print('BIENVENIDO a el contador de palabras')
    lista= []
    palabra = ''
    while palabra != 'stop':
        palabra = input('Introduce la palabra que quieres contar, para parar escribe stop: ')
        lista.append(palabra)
    desicion(lista)


if __name__ == '__main__':
    inicio()
