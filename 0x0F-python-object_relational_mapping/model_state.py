#!/usr/bin/python3
"""
Class defination of state
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    initialises table attributes
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))


if __name__ == '__main__':
    pass
