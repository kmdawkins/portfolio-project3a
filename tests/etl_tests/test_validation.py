import pandas as pd
import pytest
from loguru import logger
import sys
from etl_pipeline.utils.validation import validate_columns

# Ensure loguru writes to stdout for capture during tests
logger.remove()  # Remove the default sink
logger.add(sys.stdout, level="INFO")  # Add stdout sink to capture logs

@pytest.mark.validation  # Mark the function as a validation test
def test_validate_columns_pass(caplog):
    """Test validate columns with all required columns present."""
    df = pd.DataFrame(columns=[
        'payment_no', 'transaction_date', 'campaign_id', 'description',
        'contract_no', 'purchase_order', 'purchase_requisition', 'project_no',
        'payment_entity', 'amount_usd', 'amount_cny'
    ])
    expected = df.columns.tolist()

    # Run the validation and capture logs
    with caplog.at_level("INFO"):  # Capture logs at INFO level
        validate_columns(df, expected)

    # Check that the expected log message is present in captured logs
    assert "✅ Column validation passed." in caplog.text


@pytest.mark.validation  # Mark the function as a validation test
def test_validate_columns_fail(caplog):
    """Test validate_columns raises ValueError when required columns are missing."""
    df = pd.DataFrame(columns=[
        'payment_no', 'transaction_date', 'description',  # Missing 'campaign_id', etc.
        'contract_no', 'amount_usd'
    ])
    expected = [
        'payment_no', 'transaction_date', 'campaign_id', 'description',
        'contract_no', 'purchase_order', 'purchase_requisition', 'project_no',
        'payment_entity', 'amount_usd', 'amount_cny'
    ]

    # Capture logs for validation failure
    with caplog.at_level("ERROR"):  # Capture logs at ERROR level
        with pytest.raises(ValueError) as exc_info:
            validate_columns(df, expected)

    # Check that the expected error log message is present
    assert "❌ Missing required columns" in caplog.text

