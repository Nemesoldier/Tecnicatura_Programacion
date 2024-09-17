# Comenzamos con funciones
# Definimos una funcion

def mi_funcion(): #Para identificar la funcionar utilizamos parentesis
    print("Saludos a todos los alumnos de la Tecnicatura")
mi_funcion() #Estamos llamando a la funcion
mi_funcion() #Se puede llamar a la funcion N cantidad de veces

#Desempaquetado de listas o list unpacking
def show(name, lastName):
    print(name+" "+lastName)
person = ["Ariel", "Betancud"]
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista funcion
show(*person) #Esto es lo mismo que lo anterior pero le pasamos todos junto
person2 = ("Osvaldo", "Giordanini") #Desempaquetamos a travez de una tupla
show(*person2)
person3= {"lastName": "Lucero","name":"Natalia"}
show(**person3)

numbers = [1, 2, 3, 4, 5]  # Aun con el la lista vacia se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la unica manera de que no se ejecute el else
else:
    print("Esto se termino")

#list comprehesion, lista de compresion
names = ["Paolo","Rodrigo","lupe","Pepe"]
alongP = [p for p in names if p[0]=="P"] # Esto es una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "Country": "Argentina"},
            {"name": "Corona", "Country": "Mexico"},
            {"name": "Stella Artois", "Country": "Belgium"},
           ]
Arg = [b for b in bottleC if b["Country"] == "Argentina"]
print(bottleC)
print(Arg)

#Paso de argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos los que nos ven por youtube")
    print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2("Jorge","Lucero")
mi_funcion2("Ariel","Betancud")
mi_funcion2("Analia","Pedroza")

#La palabra return en funciones
#Creamos una funcion para sumar
def sumar (a, b):
    return a + b
#resultado = sumar(78, 22)
# print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar(55,45)}")

def sumar2(a = 0, b = 0): #Le damos un valor por default
    return a + b
resultado = sumar2()
print(f"Resultado de la suma: {resultado}")
print(f"Relsultado de la suma: {sumar2(22, 66)}")

#Argumentos, variables en funciones
def listarNomres(*nombres):  #Normalmente se ultiliza: *args
    for nombre in nombres: # Se va a comvertir en una tupla
        print(nombre)
listarNomres("Lucas","Jose","Claudia","Rosa","Maria")
listarNomres("Marcos","Daniel","Romina","Pepe","Marcela","Carlos")