import mysql.connector
from mysql.connector import MySQLConnection
from configuration import DatabaseConfig


class BaseRepository:
    dbConnection: MySQLConnection = None

    # Connect to the database
    def __init__(self, config: DatabaseConfig):
        self.validate_config(config)
        self.dbConnection = mysql.connector.connect(
                host = config.host,
                user = config.user,
                password = config.password,
                database = config.database_url)

    @staticmethod
    def validate_config(config: DatabaseConfig):
        if config.host is None:
            raise ValueError("Missing host")
        if config.user is None:
            raise ValueError("Missing user")
        if config.password is None:
            raise ValueError("Missing password")
        if config.database_url is None:
            raise ValueError("Missing database_url")

    def query(self, query: str):
        with self.dbConnection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

        