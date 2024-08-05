import os
import json

def json_type_to_postgres(type_name):
    """Convert JSON schema type to PostgreSQL type."""
    type_map = {
        'string': 'VARCHAR',
        'integer': 'INTEGER',
        'number': 'NUMERIC',
        'boolean': 'BOOLEAN',
        'array': 'TEXT[]',  # Arrays of text as a general case
        'object': 'JSONB'   # Objects as JSONB
    }
    return type_map.get(type_name, 'TEXT')

def flatten_json(data, parent_key=''):
    """Flatten JSON object into a dictionary with dot notation."""
    items = []
    for k, v in data.items():
        new_key = f"{parent_key}.{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_json(v, new_key).items())
        elif isinstance(v, list):
            if len(v) > 0 and isinstance(v[0], dict):
                # Handle arrays of objects by storing them as JSONB
                items.append((new_key, 'JSONB'))
            else:
                # Handle arrays of primitives
                items.append((new_key, 'TEXT[]'))
        else:
            items.append((new_key, json_type_to_postgres(type(v).__name__)))
    return dict(items)

def generate_postgres_schema(flattened_data, table_name='data'):
    """Generate PostgreSQL schema from flattened JSON data."""
    columns = [f"    {column_name} {data_type}" for column_name, data_type in flattened_data.items()]
    schema = f"CREATE TABLE {table_name} (\n" + "\n".join(columns) + "\n);"
    return schema

def read_json_file(filepath):
    """Read JSON data from a file."""
    with open(filepath, 'r') as file:
        return json.load(file)

def save_schema_to_file(schema, filename):
    """Save PostgreSQL schema to a .txt file."""
    with open(filename, 'w') as file:
        file.write(schema)

def main():
    """Main function to process files and generate schemas."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_directory = os.path.join(script_dir, '../collected_data')
    data_directory = os.path.abspath(data_directory)
    
    files = [f for f in os.listdir(data_directory) if f.endswith('.json')]
    
    for file in files:
        filepath = os.path.join(data_directory, file)
        try:
            data = read_json_file(filepath)
            table_name = os.path.splitext(file)[0]  # Use the filename as the table name
            flattened_data = flatten_json(data)
            schema = generate_postgres_schema(flattened_data, table_name=table_name)
            schema_filename = os.path.join(data_directory, file.replace('.json', '_schema.txt'))
            save_schema_to_file(schema, schema_filename)
            print(f"PostgreSQL schema for {file} saved to {schema_filename}")
        except Exception as e:
            print(f"Failed to process {file}: {e}")

if __name__ == "__main__":
    main()