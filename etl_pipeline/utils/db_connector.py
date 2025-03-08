import os
from dotenv import load_dotenv
import psycopg2
from sqlalchemy import create_engine

# Load environment variables
load_dotenv()

def get_psycopg2_conn():
    """Returns a psycopg2 database connection."""
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

def get_sqlalchemy_engine():
    """Returns a SQLAlchemy database engine."""
    DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    return create_engine(DATABASE_URL)
