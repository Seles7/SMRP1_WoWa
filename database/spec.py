from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base_meta import Base


class Spec(Base):
    __tablename__ = "Spec"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)

    spec_races = relationship("RaceSpec", back_populates="spec")

    def __str__(self):
        return f"Spec {self.id} {self.title}"

    def __repr__(self):
        return str(self)