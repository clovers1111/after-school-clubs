from repository.BaseRepository import BaseRepository

class PersonRepository:
    base_repository: BaseRepository

    def __init__(self, base_repository: BaseRepository) -> None:
        self.person_db = base_repository

    def find_person_by_id(self, id):
        # Get the first tuple from the list
        return self.base_repository.query(id).first()