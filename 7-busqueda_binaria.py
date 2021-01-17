"""
Se utiliza el metodo numerico llamado biseccion, en el cual
consiste en dividir a la mitad todos los valores, y comparar en que
apartado se encuentra el valor que se necesita
"""


objetivo = int(input('Escoge un numero: '))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, objetivo) #nosregresa el valor mas alto entre dos valores
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'respuesta**2={respuesta**2 - objetivo} >= epsilon: {epsilon} ')
    print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}\n')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta

    respuesta = (alto + bajo) / 2

print(f'La raiz cuadrada de {objetivo} es {respuesta}')
