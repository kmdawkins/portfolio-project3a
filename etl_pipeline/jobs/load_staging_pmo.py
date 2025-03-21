# =====================================================================
# Script: load_staging_pmo.py
# Purpose: Extract, validate, and load PMO data to staging
# Author: Katherina Dawkins (Project 3a - Python ETL)
# Version: v2.0.0 (Modified for pipeline transition (Apache Airflow))
# =====================================================================

import pandas as pd 
from loguru import logger
from dotenv import load_dotenv
import os

from etl_pipeline.utils.db_connector import get_database_url
from etl_pipeline.utils.validation import validate_columns


# Load environment variables
load_dotenv()


# Constraints
RAW_DATA_PATH = os.path.join("data", "raw", "pmo.csv")
EXPECTED_COLUMNS = [
    'payment_no', 'transaction_date', 'campaign_id', 'description',
    'contract_no', 'purchase_order', 'purchase_requisition', 'project_no',
    'payment_entity', 'amount_usd', 'amount_cny'
]

def extract_pmo_data(path: str) -> pd.DataFrame:
    """Extract raw PMO data from CSV file"""
    try:
        logger.info(f"⬇️" Reading raw data from {path}...")
        df = pd.read_csv(path)
        logger.info(f"✅ Loaded {len(df)} rows from CSV.")
        return df
    except Exception as e:
        logger.error (F"❌ Failed to read CSV:{e}")
        raise

    def load_pmo_data_to_db(df: pd.DataFrame, db_url: str) -> None:
        """Load validated DataFrame into the staging_pmo table."""
        try:
            from sqlalchemy import create_engine
            engine = create_engine(db_url)
            logger.info("⬇️ Loading data into staging_pmo table...")
            df.to_sql("staging_pmo", engine, if_exists="replace", index=False, method="multi", chunksize=1000)
            logger.success("✅ Data loaded into staging_pmo.")
            except Exception as e:
                logger.error(f"❌ Failed to load data into staging_pmo: {e}")
                raise

    def main():
        """Main ETL orchestration for staging_pmo."""
        db_url = get_database_url()

        # Extract
        df = extract_pmo_data(RAW_DATA_PATH)

        # Validate
        validate_columns(df, EXPECTED_COLUMNS)

        # Load
        load_pmo_data_to_df(df, db_url)

    if __name__ == "__main__":
        main()