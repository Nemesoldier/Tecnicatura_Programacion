# Ejercicio 8: Menu interactivo - Cajero automatico
# Hacer un programa qye simule un cajero automatico con un saldo inicial de 1000$
# y tendra el siguiente menu de opciones:
 #1.Ingresar dinero
 #2.Retirar dinero
 #3.Mostrar dinero disponible
 #4.Salir

# Saldo inicial
saldo = 1000

# Menú interactivo
while True:
    print("\n--- Menú Cajero Automático ---")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar saldo disponible")
    print("4. Salir")

    # Solicitar opción al usuario
    opcion = int(input("Elija una opción: "))

    # Opción 1: Ingresar dinero
    if opcion == 1:
        ingreso = float(input("Ingrese la cantidad de dinero a depositar: $"))
        if ingreso > 0:
            saldo += ingreso
            print(f"Has depositado ${ingreso}. Tu nuevo saldo es: ${saldo}")
        else:
            print("La cantidad ingresada debe ser positiva.")

    # Opción 2: Retirar dinero
    elif opcion == 2:
        retiro = float(input("Ingrese la cantidad de dinero a retirar: $"))
        if 0 < retiro <= saldo:
            saldo -= retiro
            print(f"Has retirado ${retiro}. Tu nuevo saldo es: ${saldo}")
        else:
            print("No puedes retirar más de lo que tienes o una cantidad negativa.")

    # Opción 3: Mostrar saldo disponible
    elif opcion == 3:
        print(f"Tu saldo actual es: ${saldo}")

    # Opción 4: Salir
    elif opcion == 4:
        print("Gracias por utilizar el cajero automático.")
        break

    # Si la opción es inválida
    else:
        print("Opción no válida, por favor elija una opción entre 1 y 4.")
