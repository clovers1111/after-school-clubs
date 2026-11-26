from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from domain.TablesConstants import TablesConstants
from entity.BaseEntity import BaseEntity


class ClubEntity(BaseEntity):
    __tablename__ = TablesConstants.CLUB

    name: Mapped[str] = mapped_column("clubName", String(60), primary_key=True)
