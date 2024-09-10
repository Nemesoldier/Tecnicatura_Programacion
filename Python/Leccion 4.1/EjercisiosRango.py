#Ejercisio python 1: Iterar nn rango de 0 a 10 e imprimir los numeros divisibles entre 3.
for i in range(11):  # Itera desde 0 hasta 10 (el 11 no se incluye)
    if i % 3 == 0:  # Verifica si el número es divisible entre 3
        print(i)
#Ejercisio 2, crear un rango de numeros de 2 a 6 e imprumirlos
for i in range(2, 7):  # Crea un rango de 2 a 6 (el 7 no se incluye)
    print(i)  # Imprime cada número en el rango
#Ejercisio 3, Crear un rango de 3 a 10 pero con incremento de 2 en 2 en lugar de 1 en 1
for i in range(3, 11, 2):  # Crea un rango de 3 a 10 con incremento de 2
    print(i)  # Imprime cada número en el rango

    # Creamos una lista
lista = [1, 2, 3, "Ariel", 7, 7, 3, "Alberto", 5, "Ariel"]
conjunto = set(lista)
print(conjunto)