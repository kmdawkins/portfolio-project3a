import os
from dotenv import load_dotenv


def configure_airflow_env():
    load_dotenv()

    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    os.environ["AIRFLOW_HOME"] = os.getenv("AIRFLOW_HOME")
    os.environ["AIRFLOW_DATABASE_SQL_ALCHEMY_CONN"] = (
        f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
    os.environ["AIRFLOW_CORE_EXECUTOR"] = "LocalExecutor"
