"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Create SQLAlchemy engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session instance
    session = Session()

    # Query the State table and retrieve the first result
    result = session.query(State).order_by(State.id).first()

    # Print the result or "Nothing" if the table is empty
    if result is not None:
        print("{}: {}".format(result.id, result.name))
    else:
        print("Nothing")
