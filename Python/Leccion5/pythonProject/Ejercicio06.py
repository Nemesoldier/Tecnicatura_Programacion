# Ejercicio 6: tabla de multiplicar
# Hacer un programa que pida un numero por teclado y guarda en una lista su tabla de multiplicar
# hastas el 10. Por ejemplo si digita el 5, la listra tendra : 5,10,15,20,25

numero = int(input("Digite un numero: "))
lista = []# Creamos una lista vacia
for i in range(1,11):
    lista.append(i*numero)
print(f"\nTabla de multiplicar del {numero}: \n {lista}")

for indice,i in enumerate(lista):
    print(f"{numero} x {i} = {lista[indice]}") #Este ciclo es para ver el formato de una tabla de multiplicar