import mysql.connector
from db import get_db_connection

def verify_user(name, passwd):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT name, passwd from user where name = %s",
                   (name,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user and user["passwd"] == passwd:
        return user
    return None

    