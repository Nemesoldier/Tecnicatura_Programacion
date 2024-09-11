# Ejercicio 7: Juego adivina el numero
# realizar un juego para adivinar un numero. para ello se debe generar un numero aleatorio entre 1 -100
# luego ir pidiendo numeros indicando "es mayor" o "es menor" segun sea mayor o menor
#con respecto al N. El proceso termina cuando el usuario acierta y alli se debe mostrar el numero de intentos.

import random
print("\t.: Juego adivina el numero:.")

# Generar un número aleatorio entre 1 y 100
numero_aleatorio = random.randint(0,100)

# Inicializar el contador de intentos
intentos = 0

# Juego de adivinanza
while True:
    # Pedir al usuario que ingrese un número
    numero_usuario = int(input("Adivina el número (entre 1 y 100): "))

    # Incrementar el contador de intentos
    intentos += 1

    # Comprobar si el número es mayor, menor o si acertó
    if numero_usuario < numero_aleatorio:
        print("El número es mayor.")
    elif numero_usuario > numero_aleatorio:
        print("El número es menor.")
    else:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
