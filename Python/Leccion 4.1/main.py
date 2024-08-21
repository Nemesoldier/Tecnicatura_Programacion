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















