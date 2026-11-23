from domain import TablesConstants
from repository.BaseRepository import BaseRepository

# clubName
class ClubRepository:
    base_repository: BaseRepository

    def __init__(self, base_repository: BaseRepository) -> None:
        self.base_repository = base_repository

    def find_all_clubs(self):
        query = "SELECT * FROM %s" % TablesConstants.TablesConstants.CLUB
        return self.base_repository.query(query)