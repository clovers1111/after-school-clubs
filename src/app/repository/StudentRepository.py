from flask_sqlalchemy.session import Session
from sqlalchemy import select
from sqlalchemy.orm import scoped_session

from domain.TablesConstants import TablesConstants
from entity.StudentEntity import StudentEntity


class StudentRepository:

    table = TablesConstants.STUDENT

    def __init__(self, session: scoped_session[Session]) -> None:
        # We want to run everything in a session to ensure that any db operations are
        # ran in a transaction and dealt with by the framework
        self.session = session

    def find_all_students(self):
        return list(self.session.scalars(select(StudentEntity)))