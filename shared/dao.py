import os

from database import Database
from shared.db_functions import DBFunctions

db_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "../site.db"
)
db = Database(db_path)
db_functions = DBFunctions(db)
