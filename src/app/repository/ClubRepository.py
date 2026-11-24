from flask_sqlalchemy.session import Session
from sqlalchemy import Engine, select
from sqlalchemy.orm import sessionmaker, scoped_session

from entity.ClubEntity import ClubEntity

class ClubRepository:

    def __init__(self, session: scoped_session[Session]) -> None:
        # We want to run everything in a session to ensure that any db operations are
        # ran in a transaction and dealt with by the framework
        self.session = session

    def find_all_clubs(self):
        return list(self.session.scalars(select(ClubEntity)))