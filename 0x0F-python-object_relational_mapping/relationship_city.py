#!/usr/bin/python3
"""
class City definition
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """
    class City
    Attributes: id, name, state_id
    Table: "cities"
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
