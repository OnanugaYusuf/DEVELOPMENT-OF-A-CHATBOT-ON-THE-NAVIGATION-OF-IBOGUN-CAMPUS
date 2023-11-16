import mysql.connector

global cnx

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="navbot"
)


def handle_user_query(destination):
    cursor = cnx.cursor()

    # Construct the SQL query dynamically based on the user's input
    query = f"SELECT time_seconds FROM nav_nav WHERE destination_name = '{destination}';"
    cursor.execute(query)
    #query = "SELECT time_seconds FROM nav_data WHERE destination_name LIKE %s;"
    #cursor.execute(query, ('%' + destination + '%',))

    # Fetch the result
    result = cursor.fetchone()

    # Close the cursor
    cursor.close()

    # Check if a result was found
    if result:
        return result[0]
    else:
        return None