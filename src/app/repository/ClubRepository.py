from repository.BaseRepository import BaseRepository


class ClubRepository:
    base_repository: BaseRepository

    CLUB = "Club"

def __init__(self, base_repository: BaseRepository) -> None:
    self.base_repository = base_repository
