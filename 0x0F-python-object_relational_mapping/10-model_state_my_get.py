#!/usr/bin/python3
"""
A script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""


if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # creating connection to MySQL DB
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # mysql://root:3778@localhost:3306/hbtn_0e_6_usa

    Session = sessionmaker(bind=engine)

    session = Session()

    state_id = session.query(
        State.id).filter(State.name.like('(?i)[sys.argv[4]]')).first()

    if state_id:
        print(state_id[0])
    else:
        print('Not found')

    session.close()
