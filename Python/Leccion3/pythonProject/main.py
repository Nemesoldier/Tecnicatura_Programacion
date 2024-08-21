
#Cliclo while (mientras o durante)

"""contador = 0
while contador < 78:
    print("Ejecutamos el ciclo while" ,contador)
    contador += 1
else:
    print("Fin del ciclo while")"""

""" maximo = 5
contador = 0
while contador <= maximo:
    print(contador)
    contador += 1"""

"""maximo = 1
contador = 5
while contador >= maximo:
    print(contador)
    contador -= 1"""

#Ciclo for

"""cadena = "hola"
for letra in cadena:
    print(letra)
else:
    print("Fin del ciclo for")"""

#Palabra reservada break

for letra in "Argentina":
    if letra == "a":
        print(f"Letra encontrada: {letra}")
        break
else:
    print("Fin del ciclo for")

#Palabra reservada continue

for i in range(6):
    if i % 2 == 0:
        print(f"valor {i}")

for i in range(6):
    if i % 2 != 0:
        continue
    print(f"valor {i}")