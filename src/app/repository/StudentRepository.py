from repository.BaseRepository import BaseRepository


class StudentRepository:
    base_repository: BaseRepository

    STUDENT = "Student"

def __init__(self, base_repository: BaseRepository) -> None:
    self.base_repository = base_repository
