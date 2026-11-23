from configuration import DatabaseConfig as dbConfig
from entity.ClubEntity import ClubEntity
from repository.BaseRepository import BaseRepository
from repository.ClubRepository import ClubRepository
from controller import HomeController
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

club_repository = ClubRepository(base_repository)
club_data = club_repository.find_all_clubs()
home_controller = HomeController()



# Test data - should be removed
some_string = person_repository.find_all_people()
print(some_string)