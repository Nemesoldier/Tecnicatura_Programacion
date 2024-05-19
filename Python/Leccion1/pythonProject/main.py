'''
miVariable = 3
print(miVariable)
miVariable = "a"
print(miVariable)
miVariable = "Hola a todos mundo los gays que estan leyendo"
print(miVariable)
b = 3
a = 3
z = a + b
print(id(z))

a = True
print(type(a))

# Tipos, int, float, string, bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas (String)
miGrupoFavorito = "Los Redondos"+" "+"Soda Stereo"
caracteristicas = "Son las mejores bandas del rock argentino"
print("Mi grupo favorito es: ", miGrupoFavorito, caracteristicas)

numero1 = 6
numero2 = 6
print(int(numero1)+int(numero2))

#Tipos boleanos (bool)
miBoo = 3 > 2
print(miBoo)

if miBoo:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

#Procesar la entrada del usuario, funcion input
#resultado = input("Digite un numero: ")
#print(resultado)

#Conversion de la entrada de datos, funcion input
#numero1 = int(input("Escibe el primer numero: "))
#numero2 = int(input("Escribe el segundo numero: "))
#resultado = numero1 + numero2
#print("El resultado de la suma es: ",resultado)

#Ejercisios 3.8
#libro =input("Digite el nombre del libro: ")
#autor =input("Digite el autor del libro: ")
#print(libro,"fue escrito por:",autor)

dia = input("¿Que tal estuvo el dia hoy?:")
print("Del 1 al 10 ¿Como estuvo tu dia? :",dia)
'''
"""
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
#print("El resultado de la suma es:",suma)
print (f"El resultado de la suma es: {suma}")
resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")
multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicacion es: {multiplicacion}")
division = operandoA / operandoB
print(f"El resultado de la division es: {division}")
division = operandoA // operandoB
print(f"El resultado de la division (int) es: {division}")
modulo = operandoA % operandoB
print (f"El resultado de la division o residuo (modulo) es: {modulo}")
exponente = operandoA ** operandoB
print(f"El resultado del exponente es: {exponente}")
"""
"""
alto = int(input("Proporcione la altura del rectangulo: "))
ancho = int(input("Proporcione el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print ("Area: ",area)
print("Perimetro: ",perimetro)
"""
"""
miVariable3 = 10
print(miVariable3)
#Operador de reasignacion
miVariable3 = miVariable3 + 1
print(miVariable3)
miVariable3 += 1
print(miVariable3)
miVariable3 -= 2
print(miVariable3)
miVariable3 *= 3
print(miVariable3)
miVariable3 /= 2
print(miVariable3)
"""
"""
d = 5
b = 6
resultado = d == b
print(resultado)
#Operador diferente
resultado = d != b
print(resultado)
#Operador de resultado
resultado = d > b
print(resultado)
#Operador menor que
resultado = d < b
print(resultado)
#Operador menor o igual que
resultado = d <= b
print(resultado)
#Operador mayor o igual que
resultado = d >= b
print(resultado)
"""
"""
a = int(input("Digite un numero: "))
print(f"El residuo de la division es {a % 2}")
if a % 2 == 0:
    print(f"El valor de a es: {a} es un numero PAR")
else:
    print(f"El valor de a es: {a} es un numero IMPAR")
"""
"""
edadAdulto = 18
edadPersona = int(input("Digite su edad: "))
if edadPersona >= edadAdulto:
    print(f"Su edad es : {edadPersona} años, es mayor de edad")
else:
    print(f"Su edad es: {edadPersona} años, es menor de edad ")
"""
"""
#Operadores logicos
a = False
b = False
resultado = a and b
print(resultado)

#Operador Or
resultado = a or b
print(resultado)
#Operador not
resultado = not a
print(resultado)
"""
"""
#Ejercicio valor dentro de un rango
valor = int (input(("Digite un valor del 0 al 5: ")))
valorMin = 0
valorMax = 5
dentroRan = (valor >= valorMin and valor <= valorMax)
if dentroRan:
    print(f"El valor {valor} esta dentro del rango")
else:
    print(f"El valor {valor} esta fuera del rango")
"""
"""
#Ejercicio con el operador or, operador not
vacaciones = True
diaDescanso = False
if not vacaciones or diaDescanso:
    print("Puede asistir al juego")
else:
    print("Tiene trabajo que hacer flojo")
"""
"""
#Ejercicio Rango entre 20 y 30 años
edad = int(input("Digite su edad:"))
veinte = edad >= 20 and edad < 30
print(veinte)
treinta = edad >= 30 and edad < 40
print(treinta)

if veinte:
    print("Estas dentro del rango de los (20' 0 ) años " )
elif treinta:
    print("Estas dentro del rango de los (30'0) años")
else:
    print("No estas dentro del rango de los (20 '0) a (30 '0) años " )
"""
"""
#Ejercicio mayor de 2 numeros
numero1 = int(input("Digite el numero 1: "))
numero2 = int(input("Digite el numero 2: "))
if numero1 > numero2:
    print("El numero 1 es el mayor")
else:
    numero2 > numero1
    print("El numero 2 es el mayor")
"""
print("Digite los siguiente datos del libro")
nombre = input("Digite el nombre del libro: ")
id = int(input("Digite el ID del libro: "))
precio = float(input("Digite el precio del libro: "))
envioGra = input("Indicar si el libro es gratuito True/False: ")
if  envioGra == "True":
    envioGra = True
elif  envioGra == "False":
    envioGra = False
else:
    envioGra = "El valor es incorrecto, debe colocar si es True o False"
print(f"""
        Nombre: {nombre}
        ID: {id}
        Precio {precio}
        Envio Gratis?: {envioGra}
""")