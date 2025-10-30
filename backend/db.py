from sqlalchemy import create_engine
from config import DB_URI

engine = create_engine(DB_URI)

def get_connection():
    conn = engine.connect()
    return conn
