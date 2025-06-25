import psycopg2  # Esto es para poder conectarnos a Postgres

conexion = psycopg2.connect(
    user='postgres',
    password='2122',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s' #Placeholder
            id_persona = input("Digite un numero: ")
            cursor.execute(sentencia , (id_persona ,)) # De est manera ejecutamos la sentencia
            registros = cursor.fetchone() # Recuperamos todos los registros que serán una lista
            print(registros)

except Exception as e:
    print(f'Ocurrió un error: {e}')

finally:
    conexion.close()
# https://www.psycopg.org/docs/usage.html