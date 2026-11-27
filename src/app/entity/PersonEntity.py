from typing import Optional

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from domain.TablesConstants import TablesConstants
from entity.BaseEntity import BaseEntity
from entity.LocationEntity import LocationEntity

# Still missing cascade deletion and updating
class PersonEntity(BaseEntity):
    __tablename__ = TablesConstants.PERSON

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column("firstName", String(20))
    last_name: Mapped[str] = mapped_column("lastName", String(60))
    address_id: Mapped[Optional[int]] = mapped_column("address",
        ForeignKey(f"{TablesConstants.LOCATION}.id"))

    address: Mapped[Optional["LocationEntity"]] = relationship()



