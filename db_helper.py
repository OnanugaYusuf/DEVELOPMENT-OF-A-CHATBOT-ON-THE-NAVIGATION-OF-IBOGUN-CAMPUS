import mysql.connector
import os

# Define the database configuration using environment variables
DB_CONFIG = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'root'),
    'password': os.environ.get('DB_PASSWORD', 'root'),
    'database': os.environ.get('DB_NAME', 'navbot'),
}

# Establish a global connection to the database
cnx = mysql.connector.connect(**DB_CONFIG)


def handle_user_query(destination):
    cursor = cnx.cursor()

    # Construct the SQL query dynamically based on the user's input
    query = f"SELECT time_seconds FROM nav_nav WHERE destination_name = '{destination}';"
    cursor.execute(query)

    # Fetch the result
    result = cursor.fetchone()

    # Close the cursor
    cursor.close()

    # Check if a result was found
    if result:
        return result[0]
    else:
        return None
