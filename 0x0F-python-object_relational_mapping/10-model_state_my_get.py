#!/usr/bin/python3
"""
prints the State object with the name passed as argument
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter_by(name=sys.argv[4]).first()

    if result:
        print('{:d}'.format(State.id))
    else:
        print('Not found')
