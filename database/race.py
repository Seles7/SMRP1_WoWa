from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base_meta import Base


class Race(Base):
    __tablename__ = "Race"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)

    race_specs = relationship("RaceSpec", back_populates="race")

    def __str__(self):
        return f"Race {self.id} {self.title}"

    def __repr__(self):
        return str(self)