from repository.BaseRepository import BaseRepository

# All Person queries should be written and passed through here
class PersonRepository:
    base_repository: BaseRepository

    # Table is case-sensitive
    PERSON = "Person"

    def __init__(self, base_repository: BaseRepository) -> None:
        self.base_repository = base_repository

    def find_all_people(self):
        query = "SELECT * FROM %s" % PersonRepository.PERSON
        return self.base_repository.query(query)

    def find_person_by_id(self, id):
        query = "SELECT * FROM %s WHERE id = %s" % (PersonRepository.PERSON, id)
        # Return the first tuple from the list
        return self.base_repository.query(query)