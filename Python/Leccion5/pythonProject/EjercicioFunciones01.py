# Ejercicio 01: Crear una funcion para sumar valores recibidos de tipo
# Numericos, utilizando argumentos variables *args cini parametro de la
# funcion y agregar como resultado la suma de todos los valores pasados como argumentos.

def sumar_valor(*args):  # Recibimos una candtidad de parametros indefinidos
    resultado = 0
    #Iteramos cada elemento
    for valor in args:
        resultado += valor
    return resultado


#Llamamos a la funcion
print(sumar_valor(3, 5, 9, 2, 1))
