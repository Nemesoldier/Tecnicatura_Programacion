# Ejercicio 11: Agenda telefonica
# Hacer un programa que simule una ageneda de contacos. Crear un
# Diccionario donde la clave sea el nombre del usuario y el valor
# sea el telefono, el programa tendra el siguiente menu de opcicones:
#           .1 Nuevo contacto
#           .2 Borrar contacto
#           .3 Ver conctactos existentes
#           .4 Salir

agenda = {}
while True:
    print("\t.:Menu:.")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    opcion = int(input("Digite una opcion de menu: "))
    if opcion == 1:
        nombre = input("Digite el nombre del contacto: ")
        telefono = input("Digite el numero de telefono: ")
        if nombre not in agenda:
            agenda[nombre] = telefono
            print("Contacto agregado exitosamente!")
        else:
            print("Este contacto ya existe")
    elif opcion == 2:
        nombre = input("Digite el nombre del contacto: ")
        if nombre in agenda:
            del(agenda[nombre])
            print("Se ha eliminado el contacto ")
        else:
            print("Este contacto no existe")
    elif opcion == 3:
        print("Agenda de contactos")
        for clave, valor in agenda.items():
            print(f"Nombre: {clave}, Telefono: {valor}")
    elif opcion == 4:
        print("Salio de la agenda")
        break
    else:
        print("Digite una opcion correcta")
    print()
