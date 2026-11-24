from sqlalchemy import create_engine

from configuration import DatabaseConfig as dbConfig
from entity.ClubEntity import ClubEntity
from repository.BaseRepository import BaseRepository
from repository.ClubRepository import ClubRepository
from controller import ClubController
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Configuration
config = dbConfig.DatabaseConfig.from_file()

logging.info("Database config loaded with host %s user %s and database %s"
            % (config.host, config.user, config.database_name))

# Allowing students to join clubs

engine = create_engine(config.host, pool_pre_ping=True)

base_repository = BaseRepository(config)
club_repository = ClubRepository(base_repository)


club_data = club_repository.find_all_clubs()
home_view = HomeView(club_data, ClubEntity.get_headers())
home_controller = ClubController(club_repository, home_view)
home_view.set_controller(home_controller)