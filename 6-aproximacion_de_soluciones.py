"""
Nos permite este algoritmo hacercarnos a una solucion de forma mas cerca,
1. No podemos ser mas precisos y mas rapidos para este algoritmo

"""

objetivo = int(input('Escoge un numero: '))
epsilon = 0.1
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada {objetivo}')
else:
    print(f'La raiz cudrada de {objetivo} es {respuesta}')
