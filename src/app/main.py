from configuration import DatabaseConfig as dbConfig
from repository.BaseRepository import BaseRepository
from repository.PersonRepository import PersonRepository
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Configuration
config = dbConfig.DatabaseConfig.from_file()

logging.info("Database config loaded with host %s user %s and database %s"
            % (config.host, config.user, config.database_name))

base_repository = BaseRepository(config)

person_repository = PersonRepository(base_repository)

# Test data - should be removed
some_string = person_repository.find_all_people()
print(some_string)