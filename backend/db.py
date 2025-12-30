import mysql.connector
from config import Config

def get_db_connection():
    return mysql.connector.connect(
        host = Config.db_host,
        user = Config.db_user,
        password = Config.db_password,
        name = Config.db_name
    )
