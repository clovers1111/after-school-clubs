from repository.BaseRepository import BaseRepository

# All Person queries should be written and passed through here
class PersonRepository:
    base_repository: BaseRepository

    def __init__(self, base_repository: BaseRepository) -> None:
        self.base_repository = base_repository

    def find_person_by_id(self, id):
        query = "SELECT * FROM Person WHERE id = %s" % id
        # Return the first tuple from the list
        return self.base_repository.query(query).first()