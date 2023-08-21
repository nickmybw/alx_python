"""
Module documentation: This script lists all State objects from the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_all_states(username, password, db_name):
    """
    Function documentation: Connects to the MySQL database and retrieves all State objects.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.

    Returns:
        None.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    fetch_all_states(username, password, db_name)
