import os
import json
import psycopg2

def get_latest_file_in_directory(directory, extension):
    """
    Get the latest file in a directory with a specific extension.
    
    :param directory: Directory to search for files.
    :param extension: File extension to look for.
    :return: Path to the latest file or None if no files are found.
    """
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(extension)]
    if not files:
        return None
    latest_file = max(files, key=os.path.getmtime)
    return latest_file

def insert_data_from_json(file_path, table_name, columns, conflict_columns):
    """
    Insert data from a JSON file into a PostgreSQL table.
    
    :param file_path: Path to the JSON file.
    :param table_name: Name of the PostgreSQL table.
    :param columns: List of columns in the table.
    :param conflict_columns: List of columns to check for conflicts (used in ON CONFLICT statement).
    """
    with open(file_path, 'r') as file:
        data = [json.loads(line) for line in file]

    if not data:
        print(f"No data found in {file_path}")
        return

    placeholders = ', '.join(['%s'] * len(columns))
    columns_str = ', '.join(columns)
    conflict_columns_str = ', '.join(conflict_columns)
    
    query = f"""
        INSERT INTO {table_name} ({columns_str})
        VALUES ({placeholders})
        ON CONFLICT ({conflict_columns_str}) DO NOTHING
    """

    conn = psycopg2.connect(
        host="localhost",
        database="datasource",
        user="anhcu",
        password="admin"
    )
    cur = conn.cursor()
    
    for record in data:
        values = [record[col] for col in columns]
        cur.execute(query, values)

    conn.commit()
    cur.close()
    conn.close()
    print(f"Inserted data into {table_name}")

def load_json_to_db_3():
    # Define the directory and file extension
    directory = '/home/anhcu/Final_ETL_App/etl-app/backend/data/processed/transformed_to_database_companies'
    extension = '.json'

    # Get the latest file in the directory
    latest_file = get_latest_file_in_directory(directory, extension)
    
    # Define the table name, columns, and conflict columns
    table_name = 'companies'
    columns = [
        "company_exchange_id", "company_industry_id", "company_sic_id", 
        "company_name", "company_ticket", "company_is_delisted", 
        "company_category", "company_currency", "company_location"
    ]
    conflict_columns = ['company_ticket', 'company_is_delisted']
    
    # Insert data from the JSON file into the PostgreSQL table
    insert_data_from_json(latest_file, table_name, columns, conflict_columns)

# load_json_to_db_3()