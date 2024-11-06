#!/usr/bin/python3
"""
This script prints all City objects
from the database hbtn_0e_14_usa:
"""

from model_state import Base, State
from model_city import City
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

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.commit()
    session.close()
