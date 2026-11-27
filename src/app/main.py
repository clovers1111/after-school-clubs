from configuration import DatabaseConfig as dbConfig
from app import init_app
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Configuration
config = dbConfig.DatabaseConfig.from_file()

logging.info("Database config loaded with host %s, user %s, and database %s"
            % (config.host, config.user, config.database_name))

init_app(config)