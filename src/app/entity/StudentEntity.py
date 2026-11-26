from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from domain.TablesConstants import TablesConstants
from entity.BaseEntity import BaseEntity
from entity.PersonEntity import PersonEntity


class StudentEntity(BaseEntity):
    __tablename__ = TablesConstants.STUDENT

    id: Mapped[int] = mapped_column(ForeignKey(f"{TablesConstants.PERSON}.id"), primary_key=True)
    grade: Mapped[int] = mapped_column()
    # Missing cascade deletion
    person: Mapped[PersonEntity] = relationship()

