#!/usr/bin/python3
"""
A script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func


def main():
    """
    Deletes all State objects with a name containing
    the letter a from the database hbtn_0e_6_usa
    """
    username, passwd, database = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, passwd, database), pool_pre_ping=True)

    # binde session maker to the engine to work with sql
    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(
        func.lower(State.name).like('%a%')).all()

    for states in states_to_delete:
        session.delete(states)

    session.commit()
    session.close()


if __name__ == '__main__':
    main()
