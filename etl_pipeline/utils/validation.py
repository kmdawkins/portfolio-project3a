from loguru import logger


def validate_columns(df, expected_columns):
    """Check that required columns exist in DataFrame."""
    missing = [col for col in expected_columns if col not in df.columns]
    if missing:
        logger.error(f"❌ Missing columns: {missing}")
        raise ValueError(f"Missing required columns: {missing}")
    logger.info("✅ Column validation passed.")