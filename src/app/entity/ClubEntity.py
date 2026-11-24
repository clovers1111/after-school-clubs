from sqlalchemy.orm import mapped_column, Mapped

from BaseEntity import Base

class ClubEntity(Base):
    __tablename__ = "Club"

    id: Mapped[int] = mapped_column(primary_key=True)
