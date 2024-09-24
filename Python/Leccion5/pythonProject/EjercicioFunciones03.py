# Ejercicio 3: Funcion recursiva
# Imprimir numeros de 5 a 1 de manera descendente usando funciuones recursivas
# Puede ser cualquier valor positivo, por ejemplo de pasamos el valor de 5, debe imprimir:
# 5
# 4
# 3
# 2
# 1
def imprimir_numeros_recursivos(numero):
    if numero >= 1:  #Caso base
        print(numero)
        imprimir_numeros_recursivos(numero-1) # Caso recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        print("Valor ingresado incorrecto.. ")
imprimir_numeros_recursivos(5)  #Tarea que el numero lo ingrese el usuario