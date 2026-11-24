from repository import ClubRepository
from flask import Flask, app


# Controller sits directly under the view and
# manages the view's state directly
class ClubController:
    clubs_repository = None

    def find_clubs(self):
        return self.clubs_repository.get_clubs()
