from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from domain.TablesConstants import TablesConstants
from entity.BaseEntity import BaseEntity
from entity.PersonEntity import PersonEntity


class ClubEntity(BaseEntity):
    __tablename__ = TablesConstants.FACULTY

    id: Mapped[int] = mapped_column(ForeignKey(f"{TablesConstants.PERSON}.id"), primary_key=True)
    department: Mapped[str] = mapped_column(String(50))
    # Missing cascade deletion
    person: Mapped[PersonEntity] = relationship()

