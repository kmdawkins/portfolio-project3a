# ==========================================================
# Script: load_staging_pmo.py
# Purpose: Load raw PMO data into staging_pmo table for ETL pipeline
# Author: Katherina Dawkins (Project 3A - Python ETL)
# Version: v1.1.0 (Added column validation - DE best practice)
# ==========================================================

import pandas as pd
from sqlalchemy import create_engine
from loguru import logger
from dotenv import load_dotenv
import os

# ------------------------------
# 1. Load Environment Variables
# ------------------------------
load_dotenv()

# ------------------------------
# 2. Database Connection Setup
# ------------------------------
DATABASE_URL = os.getenv('DATABASE_URL')

if not DATABASE_URL:
    logger.error("DATABASE_URL is not set. Please check your .env file.")
    raise ValueError("Missing DATABASE_URL for PostgreSQL connection.")

engine = create_engine(DATABASE_URL)

# ------------------------------
# 3. Load CSV File into DataFrame
# ------------------------------
RAW_DATA_PATH = 'data/raw/pmo.csv'

try:
    logger.info("Reading raw PMO data from CSV...")
    df = pd.read_csv(RAW_DATA_PATH)
    logger.info(f"Successfully read {len(df)} rows.")
except Exception as e:
    logger.error(f"Failed to read CSV file: {e}")
    raise

# ------------------------------
# 4. Validate DataFrame Columns
# ------------------------------
# Define expected columns (EXPLICIT SCHEMA CONTRACT)
EXPECTED_COLUMNS = [
    'payment_no',
    'transaction_date',
    'campaign_id',
    'description',
    'contract_no',
    'purchase_order',
    'purchase_requisition',
    'project_no',
    'payment_entity',
    'amount_usd',
    'amount_cny'
]

# Perform validation check
actual_columns = list(df.columns)
missing_columns = [col for col in EXPECTED_COLUMNS if col not in actual_columns]
extra_columns = [col for col in actual_columns if col not in EXPECTED_COLUMNS]

if missing_columns:
    logger.error(f"❌ Missing columns: {missing_columns}")
    raise ValueError(f"Missing expected columns: {missing_columns}")

if extra_columns:
    logger.warning(f"⚠️ Extra unexpected columns found: {extra_columns} (will be ignored if not in staging table)")

logger.success("✅ DataFrame columns validated successfully. Ready to load data.")

# ------------------------------
# 5. Load DataFrame into staging_pmo
# ------------------------------
try:
    logger.info("Loading data into staging_pmo table...")
    df.to_sql('staging_pmo', engine, if_exists='replace', index=False, method='multi', chunksize=1000)
    logger.success("✅ Data successfully loaded into staging_pmo.")
except Exception as e:
    logger.error(f"Failed to load data into staging_pmo: {e}")
    raise
