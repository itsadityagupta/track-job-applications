import os.path
import sqlite3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from track.app_functions import get_conn_string
from track.job_application import Base
from track.logger import logger

Session = sessionmaker()


class Database:
    """Initializes database connection"""

    def __init__(self, db_path: str, echo: bool = False):
        self.conn = None
        self.engine = None
        self.connection_string = get_conn_string(db_path)
        self.create_db(db_path, echo)
        self.session: Session = Session(bind=self.engine)

    def create_conn(self, db_path: str):
        """Creates a connection to the database"""

        if not self.conn:
            self.conn = sqlite3.connect(db_path)
            logger.info("Connection to db created successfully!")
        else:
            logger.warning("Connection already established!")

    def create_engine(self, echo: bool):
        """Create an engine for sqlalchemy to bind the datamodels"""

        if not self.engine:
            self.engine = create_engine(self.connection_string, echo=echo)
            logger.info("Engine created successfully!")
        else:
            logger.warning("Engine already created!")

    def create_db(self, db_path: str, echo: bool):
        """Main function to create the database"""
        # TODO: use less lines of code
        if os.path.isfile(db_path):
            self.create_engine(echo)
            Base.metadata.create_all(self.engine)
            logger.info("Database already created.")
            # TODO: Add option to delete the file and recreate the DB (force create)
        else:
            self.create_conn(db_path)
            self.create_engine(echo)
            Base.metadata.create_all(self.engine)
            logger.info(f"Database created at {db_path}.")
