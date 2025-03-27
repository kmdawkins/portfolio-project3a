import os
from dotenv import load_dotenv


def configure_airflow_env():
    load_dotenv()

    os.environ["AIRFLOW_HOME"] = os.getenv("AIRFLOW_HOME")
    os.environ["AIRFLOW_DATABASE_SQL_ALCHEMY_CONN"] = (
        f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    os.environ["AIRFLOW_CORE_EXECUTOR"] = "LocalExecutor"

assert os.environ["AIRFLOW_HOME"], "AIRFLOW_HOME is not set"
