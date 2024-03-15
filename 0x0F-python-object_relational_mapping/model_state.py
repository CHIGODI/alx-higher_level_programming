#!/usr/bin/python3
"""
Class defination of State inherits from Base
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import (create_engine)

Base = declarative_base()


class State(Base):
    """
    initialises table attributes
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                unique=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)


# if __name__ == "__main__":
#     engine = create_engine('mysql+mysqldb://'
#                            'root:3778@localhost:3306/'
#                            'hbtn_0e_6_usa')
#     Base.metadata.create_all(engine)
