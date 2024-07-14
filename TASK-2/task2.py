import psycopg2

# Set up database connection details
db_config = {
    'host': 'localhost',
    'dbname': 'mydb',
    'user': 'postgres',
    'password': 'admin',
    'port': 5432
}

# Connect to the PostgreSQL database
try:
    connection = psycopg2.connect(**db_config)
    cursor = connection.cursor()
    print("Connected to the database.")

    # Specify the table name
    table_name = 'data_csv'

    # Create a SQL query to count the rows
    count_query = f'SELECT COUNT(*) FROM {table_name}'

    # Execute the query
    cursor.execute(count_query)
    row_count = cursor.fetchone()[0]

    print(f'Total number of rows in {table_name}: {row_count}')

except Exception as e:
    print(f'An error occurred: {e}')