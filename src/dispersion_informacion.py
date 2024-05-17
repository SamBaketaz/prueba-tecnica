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

# Crear la tabla 'companies' si no existe
create_companies_table_query = """
CREATE TABLE IF NOT EXISTS companies (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255)
);
"""
cur.execute(create_companies_table_query)

# Crear la tabla 'charges' si no existe
create_charges_table_query = """
CREATE TABLE IF NOT EXISTS charges (
    id VARCHAR(50) PRIMARY KEY,
    company_id VARCHAR(50) REFERENCES companies(id),
    amount NUMERIC,
    status VARCHAR(50),
    created_at DATE,
    paid_at DATE
);
"""
cur.execute(create_charges_table_query)

# Nombre del archivo CSV
csv_file = 'data_prueba_tecnica.csv'

# Leer el archivo CSV y cargar los datos en las tablas de la base de datos
with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # Saltar la primera fila (encabezados)
    for row in reader:
        # Verificar si la fila tiene el número correcto de columnas
        if len(row) == 7:
            # Insertar datos en la tabla 'companies'
            company_insert_query = """
            INSERT INTO companies (id, name)
            VALUES (%s, %s)
            ON CONFLICT (id) DO NOTHING;  -- Evitar inserción de compañías duplicadas
            """
            cur.execute(company_insert_query, (row[2], row[1]))

            # Insertar datos en la tabla 'charges'
            charge_insert_query = """
            INSERT INTO charges (id, company_id, amount, status, created_at, paid_at)
            VALUES (%s, %s, %s, %s, %s, %s);
            """
            # Convertir cadena vacía en None para la fecha 'paid_at'
            row[-1] = row[-1] if row[-1] != '' else None
            cur.execute(charge_insert_query, (row[0], row[2], row[3], row[4], row[5], row[6])) # Pasar solo los elementos necesarios
        else:
            print("Fila no válida:", row)

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("La carga de datos ha sido exitosa.")