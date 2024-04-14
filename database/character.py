from datetime import date

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from .base_meta import Base


class Character(Base):
    __tablename__ = "Character"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(100), nullable=False)
    level = Column(Integer, nullable=False)
    id_racespec = Column(ForeignKey("RaceSpec.id"), primary_key=True)
    id_guild = Column(ForeignKey("Guild.id"), primary_key=True)

    racespec = relationship("RaceSpec", back_populates="racespec_characters")
    guild = relationship("Guild", back_populates="guild_characters")

    def __str__(self):
        return f"Character {self.id} {self.nickname} {self.level} {self.id_racespec} {self.id_guild}"

    def __repr__(self):
        return str(self)