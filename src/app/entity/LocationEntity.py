from typing import Optional

from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped, relationship

from domain.TablesConstants import TablesConstants
from entity.BaseEntity import BaseEntity


class LocationEntity(BaseEntity):
    __tablename__ = TablesConstants.LOCATION

    id: Mapped[int] = mapped_column(primary_key=True, auto_increment=True)
    location: Mapped[str] = mapped_column(String(100))
    room_number: Mapped[str] = mapped_column("roomNumber", String(10),
                                             default="",
                                             server_default="")

    __table_args__ = (
        UniqueConstraint('location', 'roomNumber'),
    )