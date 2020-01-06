#!/usr/bin/python3
""" Cities in state """
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City

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
    q = session.query(State, City).filter(State.id == City.state_id)\
                                  .order_by(City.id).all()
    for s, c in q:
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close()
