import pandas as pd
from loguru import logger


def load_csv_with_fallback(path: str, delimiters: list = [",", ";", "\t"]) -> pd.DataFrame:
    """
    Try loading a CSV using multiple delimiters.
    Returns the DataFrame if successful, otherwise raises an exception."""
    for delimiter in delimiters:
        try:
            df = pd.read_csv(path, delimiter=delimiter)
            logger.info(f"✅ Loaded CSV using delimiter: '{delimiter}' with {len(df)} rows.")
            return df
        except Exception as e:
            logger.warning (f"⚠️Failed to load with delimiter '{delimiter}': {e}")
    
    # If all delimiters fail, raise an error
    logger.error("❌ All delimiter attempts failed. Check file format.")
    raise ValueError("Unable to read CSV with provided delimiters.")