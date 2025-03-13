# ==========================================================
# Script: load_staging_pmo.py
# Purpose: Load raw PMO data into staging_pmo table for ETL pipeline
# Author: Katherina Dawkins (Project 3A - Python ETL)
# Version: v1.2.0 (Refactored for modular DB connection)
# ==========================================================

import pandas as pd
from sqlalchemy import create_engine
from loguru import logger
from dotenv import load_dotenv
import os

# ------------------------------
# 1. Load Environment Variables
# ------------------------------
load_dotenv()  # This loads variables from .env

# ------------------------------
# 2. Dynamic Database Connection URL
# ------------------------------
def get_database_url():
    """Assemble DATABASE_URL dynamically from separate .env components."""
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    if not all([db_user, db_password, db_host, db_port, db_name]):
        logger.error("❌ One or more required environment variables are missing. Please check your .env file.")
        raise ValueError("Missing required environment variables for PostgreSQL connection.")

    return f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

DATABASE_URL = get_database_url()
engine = create_engine(DATABASE_URL)

# ------------------------------
# 3. Load CSV File into DataFrame
# ------------------------------
RAW_DATA_PATH = 'data/raw/pmo.csv'

try:
    logger.info("📥 Reading raw PMO data from CSV...")
    df = pd.read_csv(RAW_DATA_PATH)
    logger.info(f"✅ Successfully read {len(df)} rows.")
except Exception as e:
    logger.error(f"❌ Failed to read CSV file: {e}")
    raise

# ------------------------------
# 4. Pre-Validation of DataFrame Columns (Optional, but Best Practice!)
# ------------------------------
expected_columns = [
    'payment_no', 'transaction_date', 'campaign_id', 'description', 
    'contract_no', 'purchase_order', 'purchase_requisition', 'project_no', 
    'payment_entity', 'amount_usd', 'amount_cny'
]

missing_columns = [col for col in expected_columns if col not in df.columns]
if missing_columns:
    logger.error(f"❌ Missing expected columns: {missing_columns}")
    raise ValueError(f"CSV file is missing required columns: {missing_columns}")

logger.info("✅ Column validation passed.")

# ------------------------------
# 5. Load DataFrame into staging_pmo
# ------------------------------
try:
    logger.info("📤 Loading data into staging_pmo table...")
    df.to_sql('staging_pmo', engine, if_exists='replace', index=False, method='multi', chunksize=1000)
    logger.success("✅ Data successfully loaded into staging_pmo.")
except Exception as e:
    logger.error(f"❌ Failed to load data into staging_pmo: {e}")
    raise
