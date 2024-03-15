#!/usr/bin/python3
"""
 A script that adds the State object “Louisiana” to the database
 hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine


def main():
    """
    Adds 'Louisiana' to states table in hbtn_0e_usa DB
    """
    username, passwd, database = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, passwd, database), pool_pre_ping=True)

    # binde session maker to the engine to work with sql
    Session = sessionmaker(bind=engine)
    session = Session()

    # Adds state to the table
    state_to_add = State(name='Louisiana')
    session.add(state_to_add)

    # saving the changes/commiting transaction
    session.commit()

    new_state_id = session.query(State).filter(State.name.collate(
        'utf8mb4_bin') == 'Louisiana').first()

    print(new_state_id.id)
    session.close()


if __name__ == '__main__':
    main()
