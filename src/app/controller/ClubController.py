import json

from flask import Blueprint, jsonify

from repository.ClubRepository import ClubRepository


def create_club_controller_bp(club_repository: ClubRepository):
    bp = Blueprint('club', __name__, url_prefix='/v1/clubs')

    @bp.route('/', methods=['GET'])
    def find_clubs():
        clubs = club_repository.find_all_clubs()
        # Build the mapped objects and then jsonify them
        return json.dumps([clubs.to_dict() for clubs in clubs])

    return bp
