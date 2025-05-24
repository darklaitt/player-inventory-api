from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database import Base

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    gold = Column(Integer, default=0)
    resources = Column(JSON, default={})
    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)  # weapon, armor, etc.
    owner_id = Column(Integer, ForeignKey("players.id"))
    owner = relationship("Player", back_populates="items")
