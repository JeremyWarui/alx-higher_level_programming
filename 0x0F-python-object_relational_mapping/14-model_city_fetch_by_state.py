#!/usr/bin/python3
"""
script that prints all cities by state
"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    st_cty = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in st_cty:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
