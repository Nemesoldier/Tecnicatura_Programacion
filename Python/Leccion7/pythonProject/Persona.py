class Persona:  # Clase base
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Encapsulado (privado por convención)
        self._edad = edad      # Encapsulado (privado por convención)

    # Getters para los atributos
    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad

    # Setters para los atributos
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_edad(self, edad):
        self._edad = edad

    def __str__(self):  #Override = sobreescribir
        return f"Persona : [ Nombre: {self._nombre} Edad: {self._edad} ]"


class Empleado(Persona):  # Clase hija de Persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo  # Encapsulado (privado por convención)

    # Getter y Setter para sueldo
    def get_sueldo(self):
        return self._sueldo

    def set_sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f"Empleado:[ Sueldo: {self._sueldo}] {super().__str__()}"

# Crear una instancia de Empleado
empleado1 = Empleado("Ariel", 40, 75000)

# Mostrar los datos utilizando los getters
print(f"Nombre: {empleado1.get_nombre()}")  # Imprime "Ariel"
print(f"Edad: {empleado1.get_edad()}")      # Imprime 40
print(f"Sueldo: {empleado1.get_sueldo()}")  # Imprime 75000

# Modificar los datos utilizando los setters
empleado1.set_nombre("Carlos")
empleado1.set_edad(45)
empleado1.set_sueldo(80000)

# Mostrar los datos nuevamente después de la modificación
print("\nDespués de la modificación:")
print(f"Nombre: {empleado1.get_nombre()}")  # Imprime "Carlos"
print(f"Edad: {empleado1.get_edad()}")      # Imprime 45
print(f"Sueldo: {empleado1.get_sueldo()}")  # Imprime 80000

# Crear otro objeto de la clase Empleado con diferentes valores
empleado2 = Empleado("Lucía", 30, 90000)

# Mostrar los datos del segundo objeto
print("\nDatos del segundo empleado:")
print(f"Nombre: {empleado2.get_nombre()}")  # Imprime "Lucía"
print(f"Edad: {empleado2.get_edad()}")      # Imprime 30
print(f"Sueldo: {empleado2.get_sueldo()}")  # Imprime 90000


#Tarea encapsular los atributos y agregar los metodos getters and setters
#Crear itri objeto, posar los datos para nombre edad y sueldo
#Mostrar esos datos, luego modificar y mostrar nuevamente

