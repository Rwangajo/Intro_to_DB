import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL Server (update with your credentials)
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password"
        )

        cursor = connection.cursor()

        # Use CREATE DATABASE IF NOT EXISTS to avoid failure if it already exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Always close the cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
