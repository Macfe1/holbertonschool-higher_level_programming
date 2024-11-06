#!/usr/bin/python3
"""
This script deletes all State objects
with a name containing the letter a from
the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Must be 4 arguments")
        sys.exit(1)

    engine = create_engine(
            f'mysql+mysqldb://{sys.argv[1]}:'
            f'{sys.argv[2]}@localhost/{sys.argv[3]}',
            pool_pre_ping=True
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    change_state = session.query(State).filter(State.name.like('%a%')).delete()

    session.commit()
    session.close()