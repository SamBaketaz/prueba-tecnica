import psycopg2
import csv

# Establecer la conexión con la base de datos
conn = psycopg2.connect(
    dbname="prueba",
    user="postgres",
    password="samuelrosaless13",
    host="localhost"
)

# Crear un cursor para ejecutar comandos SQL
cur = conn.cursor()

select_query = "SELECT * FROM prueba_tecnica;"

# Ejecutar la consulta SQL
cur.execute(select_query)

# Obtener todos los registros
rows = cur.fetchall()

# Nombre del archivo extraido
csv_file = 'extraccion_prueba_tecnica.csv'

# Escribir los datos en el CSV
with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    
    # Encabezados
    writer.writerow(['id', 'name', 'company_id', 'amount', 'status', 'created_at', 'paid_at'])

    # Escribir los datos en cada fila
    for row in rows:
        writer.writerow(row)

print("La extracción de datos {csv_file} ha sido exitosa.")
