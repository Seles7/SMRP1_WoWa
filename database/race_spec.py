from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class RaceSpec(Base):
    __tablename__ = "RaceSpec"

    id = Column(Integer, primary_key=True, autoincrement=True)
    race_id = Column(ForeignKey("Race.id"), nullable=False)
    spec_id = Column(ForeignKey("Spec.id"), nullable=False)

    racespec_characters = relationship("Character", back_populates="racespec")
    race = relationship("Race", back_populates="race_specs")
    spec = relationship("Spec", back_populates="spec_races")

    def __str__(self):
        return f"RaceSpec:{self.id} Race({self.race_id}) Spec({self.spec_id})"

    def __repr__(self):
        return str(self)