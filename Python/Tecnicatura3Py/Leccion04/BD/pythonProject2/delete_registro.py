import psycopg2 # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(user='postgres', password='2122', host='127.0.0.1', port='5432', database='test_bd')

try:
    with conexion.cursor() as cursor:
        sentencia = 'DELETE FROM persona WHERE id_persona=%s'
        entrada = input("Digite el numero de registro a eliminar: ")
        valores = (entrada,) # Es una tupla de valores
        cursor.execute(sentencia, valores) # De est manera ejecutamos la sentencia
        registros_eliminados = cursor.rowcount
        print(f'Los registros eliminados son: {registros_eliminados}')

except Exception as e:
    print(f'Ocurrió un error: {e}')

finally:
    conexion.close()
