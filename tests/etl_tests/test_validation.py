import pandas as pd
import pytest
import sys
import logging
from loguru import logger
from etl_pipeline.utils.validation import validate_columns

# ================================
# Logging Setup for Test Captures
# ================================

class InterceptHandler(logging.Handler):
    def emit(self, record):
        level = logger.level(record.levelname).name if record.levelname in logger._levels else record.levelno
        logger.log(level, record.getMessage())

# Redirect loguru logs to built-in logging so caplog can capture them
logging.basicConfig(handlers=[InterceptHandler()], level=0)
logger.remove()
logger.add(sys.stdout, level="INFO")
logger.add("logs/test_validation.log", level="INFO", rotation="500 MB", retention="7 days", compression="zip")

# ============================
# Column Validation Test Cases
# ============================

@pytest.mark.validation
def test_validate_columns_pass(caplog):
    """✅ Test that validation passes when all required columns are present."""
    df = pd.DataFrame(columns=[
        'payment_no', 'transaction_date', 'campaign_id', 'description',
        'contract_no', 'purchase_order', 'purchase_requisition', 'project_no',
        'payment_entity', 'amount_usd', 'amount_cny'
    ])
    expected = df.columns.tolist()

    with caplog.at_level("INFO"):
        validate_columns(df, expected)

    assert "✅ Column validation passed." in caplog.text


@pytest.mark.validation
def test_validate_columns_fail(caplog):
    """❌ Test that validation fails with missing columns."""
    df = pd.DataFrame(columns=[
        'payment_no', 'transaction_date', 'description',  # Missing 'campaign_id', etc.
        'contract_no', 'amount_usd'
    ])
    expected = [
        'payment_no', 'transaction_date', 'campaign_id', 'description',
        'contract_no', 'purchase_order', 'purchase_requisition', 'project_no',
        'payment_entity', 'amount_usd', 'amount_cny'
    ]

    with caplog.at_level("ERROR"):
        with pytest.raises(ValueError) as exc_info:
            validate_columns(df, expected)

    assert "❌ Missing required columns" in caplog.text
