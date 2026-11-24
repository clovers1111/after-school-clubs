from sqlalchemy.orm import mapped_column, Mapped

from entity.BaseEntity import BaseEntity


class ClubEntity(BaseEntity):
    __tablename__ = "Club"

    id: Mapped[int] = mapped_column(primary_key=True)
    currentAdvisor: Mapped[int] = mapped_column()