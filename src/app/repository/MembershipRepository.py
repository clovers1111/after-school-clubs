from repository.BaseRepository import BaseRepository


class MembershipRepository:
    base_repository: BaseRepository

    MEMBERSHIP = "Membership"

def __init__(self, base_repository: BaseRepository) -> None:
    self.base_repository = base_repository
