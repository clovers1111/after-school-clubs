from datetime import date

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from domain.TablesConstants import TablesConstants
from entity.FacultyEntity import FacultyEntity
from entity.BaseEntity import BaseEntity
from entity.ClubEntity import ClubEntity


class AdvisorEntity(BaseEntity):
    __tablename__ = TablesConstants.ADVISOR

    faculty_id: Mapped[int] = mapped_column("facultyId",
                                            ForeignKey(f"{TablesConstants.FACULTY}.id"),
                                            primary_key=True)
    club_name: Mapped[str] = mapped_column("clubName",
                                           String(60),
                                           ForeignKey(f"{TablesConstants.CLUB}.clubName"),
                                           primary_key=True)
    start_date: Mapped[date] = mapped_column("startDate", primary_key=True)
    end_date: Mapped[date] = mapped_column("endDate", primary_key=True)

    clubs: Mapped["ClubEntity"] = relationship(ClubEntity)
    faculty: Mapped["FacultyEntity"] = relationship(FacultyEntity)
