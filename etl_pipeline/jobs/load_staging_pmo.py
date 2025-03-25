# =====================================================================
# Script: load_staging_pmo.py
# Purpose: Extract, validate, and load PMO data to staging
# Author: Katherina Dawkins (Project 3a - Python ETL)
# Version: v3.0.0 (Modified for pipeline transition (Apache Airflow))
# =====================================================================

import os
import pandas as pd 
from dotenv import load_dotenv
from loguru import logger


from etl_pipeline.utils.db_connector import get_database_url
from etl_pipeline.utils.validation import validate_columns
from etl_pipeline.utils.file_checker import check_file_exists, validate_file_extension
from etl_pipeline.utils.csv_loader import load_csv_with_fallback
from etl_pipeline.utils.log_config import setup_logger

# Load environment variables
load_dotenv()

# Setup centralized logging
setup_logger(log_path="logs/staging_pmo.log")

# Constraints
RAW_DATA_PATH = os.path.join("data", "raw", "pmo.csv")
ALLOWED_EXTENSIONS = [".csv"]
EXPECTED_COLUMNS = [
    'payment_no', 'transaction_date', 'campaign_id', 'description',
    'contract_no', 'purchase_order', 'purchase_requisition', 'project_no',
    'payment_entity', 'amount_usd', 'amount_cny'
]

def load_pmo_data_to_db(df: pd.DataFrame, db_url: str) -> None:
    """Load validated DataFrame into the staging_pmo table."""
    try:
        from sqlalchemy import create_engine
        engine = create_engine(db_url)
        logger.info("⬇️ Loading data into staging_pmo table...")
        df.to_sql(
            name="staging_pmo",
            con=engine,
            schema="etl",
            if_exists="replace",
            index=False
        )
        logger.success("✅ Data loaded into staging_pmo.")
    except Exception as e:
        logger.error(f"❌ Failed to load data into staging_pmo: {e}")
        raise

def main():
    """Main ETL orchestration for staging_pmo."""
    db_url = get_database_url()

    # Pre-validation checks
    if not check_file_exists (RAW_DATA_PATH):
        raise FileNotFoundError (f"❌ File not found: {RAW_DATA_PATH}")
        
    if not validate_file_extension(RAW_DATA_PATH, ALLOWED_EXTENSIONS):
        raise ValueError(f"❌ Invalid file extension. Expected: {ALLOWED_EXTENSIONS}")
            
    # Extract with fallback delimiters
    df = load_csv_with_fallback(RAW_DATA_PATH)

    # Validate columns
    validate_columns(df, EXPECTED_COLUMNS)

    # Load to database
    load_pmo_data_to_db(df, db_url)

if __name__ == "__main__":
    main()