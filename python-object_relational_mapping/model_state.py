#!/usr/bin/python3
"""
This script defines a SQLAlchemy model for a 'State' and creates the
associated table in a MySQL database if it does not already exist.
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()


class State(Base):
     """Represents a state for a MySQL database."""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: ./6-model_state.py"
              "<username> <password> <database_name>")
        sys.exit(1)

    engine = create_engine(
            f'mysql+mysqldb://{sys.argv[1]}:'
            f'{sys.argv[2]}@localhost/{sys.argv[3]}',
            pool_pre_ping=True
            )

    Base.metadata.create_all(engine)
