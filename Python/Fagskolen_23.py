python
import mysql.connector
from mysql.connector import Error

def create_connection(user, password, host, database, port):
    try:
        connection = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=database,
            port=port
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None