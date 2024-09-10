#Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los numeros del 1 al 10, luego modificar
# Los elementos de la lista multiplicandolos por un valor ingresado por el usuario

lista = list(range(1,11))
print("Lista original")
for i in lista:
    print(i,end="-")
valor = int(input("\nDigite un valor a multiplicar: "))
#Multipliocamos todos los elementos de la lista
for indice, i in enumerate(lista): #Funcion para modificar la lista
    lista[indice] *= valor #El interador solo recorre los indices, en esta linea se multiplican
print(f"Lista final con los elementos multiplicados por{valor}")
for i in lista:
    print(i,end="-")