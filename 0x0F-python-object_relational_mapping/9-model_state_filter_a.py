#!/usr/bin/python3
"""objects that contain the letter a"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":

    mysql_usr = sys.argv[1]
    mysql_psw = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_usr, mysql_psw, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter(State.name.contains('a'))
    .order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
