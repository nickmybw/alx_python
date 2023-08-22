"""
Lists all State objects that contain the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine and session
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for states containing 'a' and sort by id
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    # Print results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
