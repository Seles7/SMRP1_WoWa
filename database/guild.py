from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base_meta import Base


class Guild(Base):
    __tablename__ = "Guild"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)

    guild_characters = relationship("Character", back_populates="guild")

    def __str__(self):
        return f"Guild {self.id} {self.title}"

    def __repr__(self):
        return str(self)