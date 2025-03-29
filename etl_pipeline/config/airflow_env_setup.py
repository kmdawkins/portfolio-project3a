import os
from dotenv import load_dotenv


def configure_airflow_env():
    load_dotenv()

    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    # Sanity check
    print(f"USER: {db_user}")
    print(f"PASS: {bool(db_password)}")  # Don't print actual password
    print(f"HOST: {db_host}")
    print(f"PORT: {db_port}")
    print(f"DB:   {db_name}")

    if not all([db_user, db_password, db_host, db_port, db_name]):
        raise ValueError("❌ One or more environment variables are missing. Please check your .env file.")

    os.environ["AIRFLOW_HOME"] = os.getenv("AIRFLOW_HOME")
    os.environ["AIRFLOW__DATABASE__SQL_ALCHEMY_CONN"] = (
        f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
    os.environ["AIRFLOW__CORE__EXECUTOR"] = "LocalExecutor"
