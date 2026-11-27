from flask_sqlalchemy.session import Session
from sqlalchemy import select
from sqlalchemy.orm import scoped_session

from domain.TablesConstants import TablesConstants
from entity.EventEntity import EventEntity


class EventRepository:

    table = TablesConstants.EVENT

    def __init__(self, session: scoped_session[Session]) -> None:
        # We want to run everything in a session to ensure that any db operations are
        # ran in a transaction and dealt with by the framework
        self.session = session

    def find_all_events(self):
        return list(self.session.scalars(select(EventEntity)))

    # Will likely need a find events by clubs method