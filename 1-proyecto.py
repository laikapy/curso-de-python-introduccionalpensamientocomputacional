"""
# proyecto de ramificaciones if
contador = 0

while contador < 100:
    print(contador)
    contador +=1
    if contador == 50:
        print('Ya llegamos a la mitad del contador y aplicaremos un break')
        break
"""
x = 0.0
for i in range(10):
    x += 0.1
    print(x)

if x == 1.0:
    print(f'x = {x}')
else:
    print(f'x != {x}')
