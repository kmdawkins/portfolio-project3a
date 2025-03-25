import os
from dotenv import load_dotenv
import psycopg2
from sqlalchemy import create_engine

# Load environment variables from .env file
load_dotenv()


def get_database_url() -> str:
    """
    Construct and return a PostgreSQL database URL.
    Format: postgresql://user:password@host:port/dbname
    """
    return (
        f"postgresql://{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/"
        f"{os.getenv('DB_NAME')}"
    )


def get_psycopg2_conn():
    """Returns a psycopg2 database connection (low-level)."""
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )


def get_sqlalchemy_engine():
    """Returns a SQLAlchemy database engine (high-level)."""
    return create_engine(get_database_url())


# Optional: Test connection when run standalone
if __name__ == "__main__":
    try:
        # Test psycopg2 connection
        conn = get_psycopg2_conn()
        print("✅ PostgreSQL psycopg2 connection successful!")
        conn.close()

        # Test SQLAlchemy engine connection
        engine = get_sqlalchemy_engine()
        with engine.connect() as conn:
            print("✅ PostgreSQL SQLAlchemy connection successful!")

    except Exception as e:
        print(f"❌ Database connection failed: {e}")
