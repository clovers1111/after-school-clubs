from repository.BaseRepository import BaseRepository


class AdvisorRepository:
    base_repository: BaseRepository

    ADVISOR = "Advisor"

def __init__(self, base_repository: BaseRepository) -> None:
    self.base_repository = base_repository
