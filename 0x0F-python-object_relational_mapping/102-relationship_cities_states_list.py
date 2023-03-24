#!/usr/bin/python3
"""
lists all city objects
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).outerjoin(City).order_by(City.id).all()

    for result in results:
        for city in result.cities:
            print("{}: {} -> {}".format(city.id, city.name, result.name))
