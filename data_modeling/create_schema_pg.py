import os
import psycopg2

# Directory where SQL schema files are stored
SCHEMA_DIR = './data_modeling'

# Database connection parameters
DB_HOST = 'localhost'  # Hostname for PostgreSQL container
DB_PORT = '5432'       # Port mapped for PostgreSQL
DB_NAME = 'mydatabase' # Your database name
DB_USER = 'user'       # Your database user
DB_PASSWORD = 'password' # Your database password

def connect_db():
    """Create a connection to the PostgreSQL database."""
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

def execute_sql_file(file_path):
    """Execute SQL commands from a file."""
    with open(file_path, 'r') as file:
        sql_commands = file.read()
    
    conn = None
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(sql_commands)
        conn.commit()
        cur.close()
        print(f"Successfully executed SQL commands from {file_path}")
    except psycopg2.Error as e:
        print(f"Error executing SQL commands from {file_path}: {e.pgcode} - {e.pgerror}")
    except Exception as e:
        print(f"Unexpected error executing SQL commands from {file_path}: {e}")
    finally:
        if conn is not None:
            conn.close()

def create_tables_from_schemas():
    """Create tables in PostgreSQL based on SQL schema files."""
    for filename in os.listdir(SCHEMA_DIR):
        if filename.endswith('.sql'):
            file_path = os.path.join(SCHEMA_DIR, filename)
            print(f"Processing file: {file_path}")
            execute_sql_file(file_path)

if __name__ == '__main__':
    create_tables_from_schemas()