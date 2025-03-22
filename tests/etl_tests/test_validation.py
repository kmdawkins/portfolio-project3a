# tests/etl_tests/test_validation.py

import pandas as pd
import pytest
from etl_pipeline.utils.validation import validate_columns

@pytest.mark.validation # Mark the function as a validation test
def test_validate_columns_pass():
    """Test validate columns with all required columns present."""
    df = pd.DataFrame(columns=[
        'payment_no', 'transaction_date', 'campaign_id', 'description',
        'contract_no', 'purchase_order', 'purchase_requisition', 'project_no',
        'payment_entity', 'amount_usd', 'amount_cny'
    ])
    expected = df.columns.tolist()


    # This should not raise an exception
    try:
        validate_columns(df, expected)
    except Exception as e:
        py.fail(f"Unexpected exception raised: {e}")


@pytest.mark.validation # Mark the function as a validation test
def test_validate_columns_fail():
    """Test validate_columns raises ValueError when required columns are missing."""
    df = pd.DataFrame(columns=[
        'payment_no', 'transaction_date', 'description', # Missing 'campaign_id', etc.
        'contract_no', 'amount_usd'
    ])
    expected = [
        'payment_no', 'transaction_date', 'campaign_id', 'description',
        'contract_no', 'purchase_order', 'purchase_requisition', 'project_no',
        'payment_entity', 'amount_usd', 'amount_cny'
    ]


    with pytest.raises(ValueError) as exc_info:
        validate_columns(df, expected)

    assert "Missing required columns" in str(exc_info.value)