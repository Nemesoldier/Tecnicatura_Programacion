#Ejercicio 3: Insertar elementos y ordenarlos
#Pedir numeros y meterlos en una lista, cuando el usuario
# introduizca un numero 0, nunestro programa dejaria de insertar
# por ultimo mostrar los numeros ordenados de menor a mayor

lista = []
salir = False
while not salir:
    numero = int(input("Digite un numero: "))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort() #La lista esta ordenada con esta funcion
print(f"\nLista ordenada: \n{lista}")