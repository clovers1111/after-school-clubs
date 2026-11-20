from repository.BaseRepository import BaseRepository


class LocationRepository:
    base_repository: BaseRepository

    LOCATION = "Location"

def __init__(self, base_repository: BaseRepository) -> None:
    self.base_repository = base_repository
