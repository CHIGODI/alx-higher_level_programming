#!/usr/bin/python3
"""
A script that lists all State objects that contain the letter a from the
database hbtn_0e_6_usa
"""


if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine, select, func
    from sqlalchemy.orm import sessionmaker

    # creating connection to MySQL DB
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # returns a list of objects
    states = session.query(State).filter(func.lower(State.name).like(
        '%a%')).order_by(State.id.asc()).all()

    for state in states:
        print(f'{state.id}: {state.name}')

    session.close()
