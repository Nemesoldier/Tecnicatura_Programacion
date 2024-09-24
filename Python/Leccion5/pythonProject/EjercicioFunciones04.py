# Ejercicio 4: Calculadora de impuestos
# Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado. (IVA)
# formula pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
# Proporcione el pago sin impuesto: 1000
# Proporcione el monto del impuesto: 21%
# El pago con impuesto: xxxx

# Definición de la función para calcular el pago con impuesto
def calcular_pago_con_impuesto(pago_sin_impuesto, porcentaje_impuesto):
    impuesto = pago_sin_impuesto * (porcentaje_impuesto / 100)
    pago_total = pago_sin_impuesto + impuesto
    return pago_total

# Solicitar los datos al usuario
pago_sin_impuesto = float(input("Proporcione el pago sin impuesto: "))
porcentaje_impuesto = float(input("Proporcione el monto del impuesto (%): "))

# Calcular el pago con impuesto
pago_con_impuesto = calcular_pago_con_impuesto(pago_sin_impuesto, porcentaje_impuesto)

# Mostrar el resultado
print(f"El pago con impuesto es: {pago_con_impuesto}")
