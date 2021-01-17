import math #impoorta las operacione matemáticas avanzadas
numero1 = int(input('Ingrese primer numero: '))
numero2 = int(input('Ingrese segundo numero: '))
num_cifras_signif = int(input('Ingrese el numero de cifras significativas: '))
if numero1 > numero2:
    print(f'El resultado de dividir: {numero2} / {numero1} = ')
    Numerador = numero2
    Denominador = numero1
elif numero2 > numero1:
    print(f'El resultado de dividir: {numero1} / {numero2} = ')
    Numerador = numero1
    Denominador = numero2
else:
    print(f'El resultado de dividir: {numero1} / {numero2} = 1')

# definiciones:
# A/B = (X,-n); donde A < B, X = representaciónen binario del numerador
# -n; es el exponente dela base 2(de binario),
# La aproximacióndela división es: A/B = X/2^n
# #####    ALGORITMO EN 3 PASOS:   ########
# 1. Estimaciónde X y calculo den
# 2. Calculo de X
# 3. Mostrar resultados con la aproximación especificada.

# ================ PROCEDIMIENTO ==================
# Estimaciónde"X"
# x <= int(2^num_cifras_signif - 1)
x = int(math.pow(2,num_cifras_signif))

# Calculo de"n"
# n = int(log2(X*B/A))
n = int(math.log2(x*Denominador/Numerador))

# Calculo de"X"
# x = int(A / B * 2 exp(n))
x = int(Numerador/Denominador*math.pow(2,n))

# finalmente A/B = X/2^n
print('===========================================================')
print(f'Resultado del Algoritmo: {Numerador}/{Denominador} = {x}/{math.pow(2,n)} ={ x / math.pow(2,n) }, para una aprox. de {num_cifras_signif} cifras significativas')
print(f'comparado a : {Numerador}/{Denominador} ={Numerador/Denominador}, considerando hasta 53 bits de precisión para numero flotante')
print('===========================================================')
