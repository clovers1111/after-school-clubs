from flask import Flask, app, Blueprint

from repository.ClubRepository import ClubRepository


def create_club_controller_bp(club_repository: ClubRepository):
    bp = Blueprint('club', __name__, url_prefix='/v1/clubs')

    @bp.route('/', methods=['GET'])
    def find_clubs(self):
        return self.clubs_repository.get_clubs()

    return bp
