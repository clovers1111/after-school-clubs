from repository.BaseRepository import BaseRepository


class EventRepository:
    base_repository: BaseRepository

    EVENT = "Event"

def __init__(self, base_repository: BaseRepository) -> None:
    self.base_repository = base_repository
