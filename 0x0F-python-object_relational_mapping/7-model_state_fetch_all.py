#!/usr/bin/python3
"""
A script that connects to a MySQL DB and list all states orderd by ID
"""
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

states = session.query(State).order_by(State.id.asc()).all()

for state in states:
    print(f'{state.id}: {state.name}')

session.close()
