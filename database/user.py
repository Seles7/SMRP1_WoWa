from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base_meta import Base


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

    user_characters = relationship("Character", back_populates="user")

    def __str__(self):
        return f"User {self.id} {self.username} {self.password}"

    def __repr__(self):
        return str(self)