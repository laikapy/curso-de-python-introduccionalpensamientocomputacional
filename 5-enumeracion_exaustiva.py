#Esto se refiere a enumerar todas las posibilidades para encontrar nuestro resultado
#Objetivo del algoritmo: encontrar la respuesta a traves de oberservar todas las posbilidades
objetivo = int(input('Escoje un numero entero que deseas saber su raiz cuadrada: '))
respuesta = 0

while respuesta**2 < objetivo: # estamos indicando que cuando respuesta sea mayor que objetivo, se detenga este bucle
    respuesta_cuadrada = respuesta**2 #guardando el valor del resultado
    print(f'{respuesta} su cuadrado es {respuesta_cuadrada}')
    respuesta +=1
if respuesta**2 == objetivo:
    print(f'la raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'el numero {objetivo} no tiene raiz exacta')
#este algoritmo nos permite observar como el comutador realiza todas las operaciones
para encontrar la raiz cuadrada de un numero, en donde al encontrar esa raiz respuesta_cuadrada
la comparara con el numero que ingresamos, si coinciden, tenemos el resultado
de lo contrario, no tiene raiz cuadrada
