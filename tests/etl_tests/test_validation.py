import pandas as pd
import pytest
from loguru import logger
from io import StringIO
from etl_pipeline.utils.validation import validate_columns

@pytest.mark.validation
def test_validate_columns_pass():
    """✅ Test that validation passes when all required columns are present."""
    df = pd.DataFrame(columns=[
        'payment_no', 'transaction_date', 'campaign_id', 'description',
        'contract_no', 'purchase_order', 'purchase_requisition', 'project_no',
        'payment_entity', 'amount_usd', 'amount_cny'
    ])
    expected = df.columns.tolist()

    log_stream = StringIO()
    logger.remove()
    logger.add(log_stream, level="INFO")

    validate_columns(df, expected)

    log_contents = log_stream.getvalue()
    assert "✅ Column validation passed." in log_contents


@pytest.mark.validation
def test_validate_columns_fail():
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

    log_stream = StringIO()
    logger.remove()
    logger.add(log_stream, level="ERROR")

    with pytest.raises(ValueError):
        validate_columns(df, expected)

    log_contents = log_stream.getvalue()
    assert "❌ Missing columns:" in log_contents
