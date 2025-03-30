"""
Purpose: Temporary debug script to test Airflow DB connection string.
Safely runs outside the DAG context for isolated troubleshooting.
"""

import os
import sys
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError


def debug_airflow_connection_string(env_path=".env"):
    # Load env vars
    if not os.path.exists(env_path):
        raise FileNotFoundError(f"❌ Env file not found at: {env_path}")
    load_dotenv(dotenv_path=env_path)

    # Load values
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    # Sanity check printout
    print(f"\n🔍 Sanity Check:")
    print(f"USER: {db_user}")
    print(f"PASS SET: {bool(db_password)}")
    print(f"HOST: {db_host}")
    print(f"PORT: {db_port}")
    print(f"DB: {db_name}\n")

    # Fail fast
    if not all([db_user, db_password, db_host, db_port, db_name]):
        raise ValueError("❌ Missing one or more required environment variables. Check .env.")

    # Construct full connection string
    conn_str = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    print(f"🔧 Connection string (masked): postgresql+psycopg2://{db_user}:****@{db_host}:{db_port}/{db_name}")

    # Try to connect
    print("\n🔌 Testing connection...")
    try:
        engine = create_engine(conn_str)
        with engine.connect() as conn:
            print("✅ Successfully connected to PostgreSQL database!")
    except OperationalError as e:
        print(f"❌ Connection failed:\n{e}")
        sys.exit(1)


if __name__ == "__main__":
    debug_airflow_connection_string()
