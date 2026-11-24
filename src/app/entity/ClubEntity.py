from sqlalchemy.orm import mapped_column, Mapped

from domain.TablesConstants import TablesConstants
from entity.BaseEntity import BaseEntity


class ClubEntity(BaseEntity):
    __tablename__ = TablesConstants.CLUB

    id: Mapped[int] = mapped_column(primary_key=True)
    currentAdvisor: Mapped[int] = mapped_column()