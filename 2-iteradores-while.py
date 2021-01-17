print('BIENVENIDO A NUESTRA LISTA')
def iterador(mylist): #imprimiremos todos los elementos de una lista
    impresion = ''
    for impresion in mylist:
        print(impresion)

#----------------------------------------------------------------------#
def condicional(desicion,mylist): #es esta funcion imprimiremos la lista
    if desicion == 'lista':
        iterador(mylist)
    elif desicion == 'no':
        print('Hasta la proxima')
    else:
        print('Ingresaste un valor incorrecto')
#----------------------------------------------------------------------#
def nombre(): #En esta funcnion ingresamos datos
    nombres = ''
    mylist = [] #declaramos nuestra lista
    while nombres != 'stop': #si dijita la palabra stop, saldremos del bucle
        nombres = input('Ingresa los nombres que quieres agregar al documento:  ')
        mylist.append(nombres) #agregamos datos a la lista con el metodo append
    #fin del bucle while
    desicion = input('Si deseas ver la lista, escribe lista, de los contrario pon no:  ')
    condicional(desicion,mylist)
#----------------------------------------------------------------------#
if __name__ == '__main__':
    nombre()
