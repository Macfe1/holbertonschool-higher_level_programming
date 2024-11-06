#!/usr/bin/python3
"""
Module to define a City class
representing a table in a database
using SQLAlchemy.
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import sys


class City(Base):
    """
    City class that represents the 'cities'
    table in the database.

    Attributes:
        id (int): The primary key for the city, automatically incremented.
        name (str): The name of the city, cannot be null.
        state_id (int): The foreign key linking to the state's id
        in the 'states' table.
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("State", backref="cities")
