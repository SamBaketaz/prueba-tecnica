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

# Nombre del archivo CSV
csv_file = 'data_prueba_tecnica.csv'

# Nombre de la tabla en la base de datos
table_name = 'prueba_tecnica'

# Crear la tabla en la base de datos si no existe
create_table_query = """
CREATE TABLE IF NOT EXISTS {} (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255),
    company_id VARCHAR(50),
    amount NUMERIC,
    status VARCHAR(50),
    created_at DATE,
    paid_at DATE
);
""".format(table_name)

cur.execute(create_table_query)
conn.commit()

# Leer el archivo CSV y cargar los datos en la tabla de la base de datos
with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # Saltar la primera fila (encabezados)
    for row in reader:
        print("Fila actual:", row)  # Impresión de depuración
        # Verificar si la fila tiene el número correcto de columnas
        if len(row) == 7:
            # Ignorar la columna 'paid_at'
            insert_query = """
            INSERT INTO {} (id, name, company_id, amount, status, created_at, paid_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
            """.format(table_name)
            # Convertir cadena vacía en None para la fecha 'paid_at'
            row[-1] = row[-1] if row[-1] != '' else None
            cur.execute(insert_query, row)
        else:
            print("Fila no válida:", row)

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("La carga de datos ha sido exitosa.")