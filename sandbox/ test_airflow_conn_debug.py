"""
Purpose: Temporary debug script to test Airflow DB connection string.
Safely runs outside the DAG context for isolated troubleshooting.
"""


import os
from dotenv import load_dotenv()



def debug_airflow_connection_string():
    load_dotenv


    # Load database connection pieces
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv ("DB_HOST")
    db_port = os.getenv ("DB_PORT")
    db_name = os.getenv ("DB_NAME")

    # Print sanity checks (don't print the actual password)
    print(f"\n🔍 Sanity Check:")
    print(f"USER: {db_user}")
    print(f"PASS SET: {bool(db_password)}")
    print(f"HOST: {db_host}")
    print(f"PORT: {db_port}")
    print(f"DB: {db_name}\n")


    # Fail early if anything is missing
    if not all ([db_user, db_password, db_host, db_port, db_name]):
        raise ValueError ("❌ Missing required environment variable(s). Check your .env file.")

    # Construct and print connection string (mask password)
    conn_str = f"postgresql+psycopg2://{db_user}:****@{db_host}:{db_port}/{db_name}"
    print(f"✅ SQLAlchemy Connection String (masked):\n{conn_str}")



if __name__ == "__main__":
    debug_airflow_connection_string()
