from repository.BaseRepository import BaseRepository


class FacultyRepository:
    base_repository: BaseRepository

    FACULTY = "Faculty"

def __init__(self, base_repository: BaseRepository) -> None:
    self.base_repository = base_repository
