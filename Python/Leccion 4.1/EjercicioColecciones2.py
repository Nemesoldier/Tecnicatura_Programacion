# Ejercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga 2 listas y que a continuacion
# cree las siguientes listas (en las quie no deben haber repeticion)
#1 Lista de palabras que aparecen en las listas
#2Lista de palabnras que aparecen en la primera lista, pero no en la segunda
#3 Lista de palabras que aparecen en la segunda lista, pero no en la primera
#4 Lista de palabras que aparecen en ambas listas

# Definir las dos listas
lista1 = [1,2,3,4,5,4,3,2,2,1,5]
lista2 = [4,5,6,7,8,4,5,6,7,7,8]

# Convertir las listas a conjuntos para eliminar duplicados y trabajar con operaciones de conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

# 1. Lista de palabras que aparecen en ambas listas (sin repetición)
lista_union = list(conjunto1 | conjunto2)  # Unión de los conjuntos

# 2. Lista de palabras que aparecen en la primera lista, pero no en la segunda
lista_diferencia1 = list(conjunto1 - conjunto2)  # Diferencia de conjunto1 respecto a conjunto2

# 3. Lista de palabras que aparecen en la segunda lista, pero no en la primera
lista_diferencia2 = list(conjunto2 - conjunto1)  # Diferencia de conjunto2 respecto a conjunto1

# 4. Lista de palabras que aparecen en ambas listas
lista_interseccion = list(conjunto1 & conjunto2)  # Intersección de los conjuntos

# Mostrar las listas resultantes
print("1. Lista de palabras que aparecen en ambas listas (sin repetición):", lista_union)
print("2. Lista de palabras que aparecen en la primera lista, pero no en la segunda:", lista_diferencia1)
print("3. Lista de palabras que aparecen en la segunda lista, pero no en la primera:", lista_diferencia2)
print("4. Lista de palabras que aparecen en ambas listas:", lista_interseccion)
