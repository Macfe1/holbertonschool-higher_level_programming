#!/usr/bin/python3
"""
This script fetches the State object that contain the
passed argument name from the database
hbtn_0e_6_usa using SQLAlchemy.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Must be 5 arguments")
        sys.exit(1)

    engine = create_engine(
            f'mysql+mysqldb://{sys.argv[1]}:'
            f'{sys.argv[2]}@localhost/{sys.argv[3]}',
            pool_pre_ping=True
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    states_name = session.query(State).filter(
        State.name == sys.argv[4]).first()

    if states_name is None:
        print("Not found")
    else:
        print(f"{states_name.id}")

    session.close()
