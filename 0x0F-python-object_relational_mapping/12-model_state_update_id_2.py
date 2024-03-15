#!/usr/bin/python3
"""
 A  script that changes the name of a State object from the database
 hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine


def main():
    """
    updates state.name with state.id=2 to 'New Mexico'
    """
    username, passwd, database = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, passwd, database), pool_pre_ping=True)

    # binde session maker to the engine to work with sql
    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_update = session.query(State).filter(State.id == 2).first()

    if state_to_update.name:
        state_to_update.name = 'New Mexico'
        session.commit()
    session.close()


if __name__ == '__main__':
    main()
