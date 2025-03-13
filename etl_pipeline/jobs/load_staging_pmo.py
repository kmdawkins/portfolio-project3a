# ==========================================================
# Script: load_staging_pmo.py
# Purpose: Load raw PMO data into staging_pmo table for ETL pipeline
# Author: Katherina Dawkins (Project 3A - Python ETL)
# Version: v1.0.1 (Secured with environment variables)
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
# 4. Load DataFrame into staging_pmo
# ------------------------------
try:
    logger.info("Loading data into staging_pmo table...")
    df.to_sql('staging_pmo', engine, if_exists='replace', index=False, method='multi', chunksize=1000)
    logger.success("Data successfully loaded into staging_pmo.")
except Exception as e:
    logger.error(f"Failed to load data into staging_pmo: {e}")
    raise
