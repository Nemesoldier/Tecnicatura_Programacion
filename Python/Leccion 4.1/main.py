#Colecciones en Python
#Las listas es lo que se conoce en otros lenguajes como arreglos o vectores

nombres = ["Martins","Mati","Matias","Naty"]
print (nombres)
print (nombres[0:2]) # Solo muentra el indice 0, 1 pero no el 2
print(nombres[:3]) #Indice a mostrar 0, 1, 2
#Desde el indice indicado hasta el final
print(nombres[1: ])
#modificamos valor dentro de la lista
nombres[2] = "Jose"
nombres[1] = "Paulo"
print(nombres)
# Iterar una lista
for nombre in nombres:   #nombre es singular, la lista es plural
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

#Preguntamos cuantos elementos tiene la lista
print(len(nombres)) # Le pasamos como parametros la lista
#Agregamos un elemento
nombres.append("marcelo")
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4,5])
nombres.append([7])
print(nombres)
#insertar un elemento en un indice especifico
nombres.insert(1,"Alberto")
print(nombres)
nombres.insert(3,"Debora")
print(nombres)
#Eliminamos un elemento
nombres.remove("Alberto")
print(nombres)
#Eliminar el ultimo elemento
nombres.pop()
print(nombres)
#Eliminar un indidice especifico
del nombres[2]
print(nombres)
#Eliminar, borrar todos los elementos
nombres.clear()
print(nombres)
#Eliminar la lista
del nombres
#print(nombres) #Aca muestra error

#Definimos una tupla
cocina = ("cuchara","cuchillo","Tenedor")
print(len(cocina))
#Acceder a un elemento para esto usamos corchetes no parentesis
print(cocina[0])
#Mostrar a la inversa
print(cocina[-1])
#Acceder a un rango
print(cocina[0:2])
#Ejemplo
verduras = ("papa",) #Una tupla necesita aunque sea un elemento: la coma
#De lo contrario solo seria un tipo string cadena

#Recorremos los elementos de la tupla
for cocinar in cocina:# print esta usando \n para saltos de lineas
    print(cocinar, end=" ") #Usamos end= para eliminar los saltos de linea

cocinaLista = list(cocina)
cocinaLista [0] = "Plato"
cocina = tuple(cocinaLista)
print("\n",cocina)

#del cocina # Esto es para eliminar la tupla

#tipo de set
planetas = {"marte", "jupiter", "venus"}
print(len(planetas)) # usamos la funcion len = lenght significa largo

#Revisar si el elemento existe dentro del set
print("marte" not in planetas)

#Agregar un elemento
planetas.add("tierra") #Add es la funcion
print(planetas)

#Eliminar elementos, puede arrojar un error si el elemento no exite
planetas.remove("jupiter") #Esta funcion si lo cologamos mal al elemento da error
print(planetas)
planetas.discard("tierra") #Esta funcion no nos presenta error si nos equivocamos
print(planetas)

#Limpiar set o conjunto
planetas.clear()
print(planetas)

#Eliminar set
del planetas
#print(planetas) #Al eliminar nos muestra error

#"Maradona": 10 Un diccionario esta compuesto por 2 elementos, una llave y un valor
#dic(key,value)
diccionario = {
    "IDE":"Integrate Development Environment",
    "POO": "Programacion orientada a objetos",
    "SABD": "Sistema de administracion de base de datos"

}
#Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

#Acceder a un diccionario con la llave (key)
print(diccionario["IDE"])

#Otra forma de recuperar un elemento
print(diccionario.get("POO"))
print(diccionario.get("SABD"))

#Modificamos los elemtnos
diccionario["IDE"] = "Entorno de desarrollo Integrado"
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: #Recorremos mostrando solo las llaves
    print(termino)
#Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

#Otras maneras de acceder a un diccionario
for termino in diccionario.keys(): #Estamos usando una funcion
    print(termino) #Muestra solo las llaves

for valor in diccionario.values(): #Usamos esta funcion para acceder al valor
    print(valor)

# Comprobar la existencia de algun elemento
print("IDE" in diccionario) #Devuelve un booleano

#Agregar un elemento
diccionario["PK"] = "Primary Key"
print(diccionario)

#Eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario
del diccionario #El diccionario se borro
#print(diccionario)

#Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2 #concatenacion
print(lista3)
lista3.extend([7, 8, 9, 1]) #Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) #Funcion para ubicar en que indice esta el valor ingresado
#print(lista3.index(0)) #esto daria error por no ser el elemento parte de la lista

#como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) #Cuenta cuantos valores iguales hay dentro de la lista

#Para poner al reves la lista
lista3.reverse()
print(lista3)

#Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

#Metodos de ordenamiento en Python
lista3.sort() #Ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True) #Ordenamos de forma descendente
print(lista3)

tupla = (4, "Hola", 6.78, [1,2,78],4,"Hola") #Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) #Accion booleana, su respuesta es de tipo booleana
#Lo que podemos usar dentro de tuplas son : index, count, len
#En tuplas se puede convertir de tupla a lista y de lista a tupla


##Repaso de set
# Para definir un conjunto

conjunto2 = set ()
conjunto1 = {"bye"}
conjunto2.add (7)
conjunto2.add("Hola")
print(conjunto2)
conjunto1.add("hola")
print(conjunto1)
print(3 not in conjunto1) #pregguntamos si el numero 3 NO esta incluido

#Como hacer la igualdad de 2 conjuntis
print(conjunto1 == conjunto2)

#Operaciones en conjunto
conjunto3 = conjunto1 | conjunto2 # La linea une los 2 conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 #Que elemento tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 #Asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # elementos que no se comparten o son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) #Aqui preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) #Preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto2)) # Si es verdadero quiere decir que el conjunto 3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

#Como saber si ambos conjuntos son disconexsos, esto es si comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) #No hay cosas en comun

#Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset # Esto hacer que el conjunto sea totalmente inmutable
# No se puede agregar, modificar ni eliminar elementos del conjunto

#Repaso diccionarios
diccionarioNuevo = {"Azul":"Blue","Rojo":"Red","Verde":"Green","Amarillo":"Yellow"}
print(diccionarioNuevo)

#como eliminar
del diccionarioNuevo["Azul"]
print(diccionarioNuevo)

#Los diccionarios pueden almacenar diferentes tipos de datos
diccinario2 = {"Ariel":{"Edad":40,"Altura":1.83},"Osvaldo":[45,1,85],"Natalia":[35,1.67]}
print(diccinario2)

seleccionArgentina = {
    10:{"Nombre":"Lionel Messi","Edad":35,"Altura":1.70,"Precio": "50 millones","Posicion":"Extremo Derecho"},
    11:{"Nombre": "Angel Di Maria","Edad":34,"Altura":1.80,"Precio":"12 Millones","Posicion":"Extremo Derecho"},
    24:{"Nombre": "Paulo Dybala","Edad":28,"Altura":1.77,"Precio":"35 Millones","Posicion":"Media Punta"},
    19:{"Nombre": "Nicolas Otamendi","Edad":34,"Altura":1.83,"Precio":"3.5 Millones","Posicion":"Defensa Central"},
    1:{"Nombre": "Franco Armani","Edad":33,"Altura":1.89,"Precio":"3.5 Millones","Posicion":"Portero"}
}
for llave, valor in seleccionArgentina.items():
    print(llave, valor)


#Agregar por lo menos 4 jugadores mas al diccionario : seleccionArgentina
print("Tenemos cargasdors en el diccionario la cantidad de jugadores: ", end=" ")
print(len(seleccionArgentina))

#Pilas usando listas
pila = [1, 2, 3]

#Agregar elementos a una pila por el final
pila.append(4)
pila.append(5)
print(pila)

#Sacamos elementos desde el final
elementoBorrado = pila.pop() #Quita el ultimo elemnto y lo guarda en en la variable
print(f"Scamos el elementos borrado {elementoBorrado}")
print(f"La pila ahora quedo asi: {pila}")

#Colas en listas
#Estructura de datos tipo fifo (first input, first output)
cola = ["Ariel","Osvaldo","Liliana","Pilar"]
#Agregamos elementos

cola.append("Natalia")
cola.append("Jose")
print(cola)

#Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)





