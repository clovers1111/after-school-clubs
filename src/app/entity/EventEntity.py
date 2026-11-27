from datetime import datetime

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from domain.TablesConstants import TablesConstants
from entity.BaseEntity import BaseEntity
from entity.ClubEntity import ClubEntity
from entity.LocationEntity import LocationEntity


class EventEntity(BaseEntity):
    __tablename__ = TablesConstants.EVENT

    club_name: Mapped[str] = mapped_column("clubName",
                                           ForeignKey(f"{TablesConstants.CLUB}.clubName"),
                                           primary_key=True)
    start_time: Mapped[datetime] = mapped_column("startTime", primary_key=True)
    end_time: Mapped[datetime] = mapped_column("endTime")
    event_type: Mapped[str] = mapped_column("eventType", String(30))
    description: Mapped[str] = mapped_column("description", String(50))
    location_id: Mapped[int] = mapped_column("locationId",
                                             ForeignKey(f"{TablesConstants.LOCATION}.id"))

    club: Mapped["ClubEntity"] = relationship()
    location: Mapped["LocationEntity"] = relationship()

