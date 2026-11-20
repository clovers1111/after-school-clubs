import mysql.connector
import logging
from mysql.connector.abstracts import MySQLConnectionAbstract
from configuration import DatabaseConfig

# BaseRepository is the generic database interfacing class we use
# to make API calls to the database; it is injected in every
# repository class.
#
# All queries should go through this class to reduce the amount of
# code repetition and creating multiple instance of the db connection
# during a single application runtime
class BaseRepository:
    dbConnection: MySQLConnectionAbstract = None

    # Connect to the database
    def __init__(self, config: DatabaseConfig):
        self.validate_config(config)
        logging.info("Connecting to database %s on host %s" % (config.database_name, config.host))
        self.dbConnection = mysql.connector.connect(
                    host = config.host,
                    user = config.user,
                    password = config.password,
                    database = config.database_name,
                    connection_timeout = config.connection_timeout)
        logging.info("Connected to database %s on host %s" % (config.database_name, config.host))

    @staticmethod
    def validate_config(config: DatabaseConfig):
        if config.host is None:
            raise ValueError("Missing host")
        if config.user is None:
            raise ValueError("Missing user")
        if config.password is None:
            raise ValueError("Missing password")
        if config.database_name is None:
            raise ValueError("Missing database_name")
        if config.connection_timeout is None:
            raise ValueError("Missing connection_timeout")

    # This is a blocking call for queries - this is intentional
    # for the time being.
    def query(self, query: str):
        with self.dbConnection.cursor() as cursor:
            logging.info("Executing query: %s" % (query))
            try:
                cursor.execute(query)
                return cursor.fetchall()
            except mysql.connector.Error as error:
                logging.error(error)