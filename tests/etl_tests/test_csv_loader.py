import pytest
import pandas as pd
from io import StringIO

# ✅ Setup logging
from etl_pipeline.utils.log_config import setup_logger
setup_logger()

from etl_pipeline.utils.csv_loader import load_csv_with_fallback

# Test 1: First delimiter fails, second one (semicolon) succeeds
def test_load_csv_with_fallback_delimiter(tmp_path):
    test_file = tmp_path / "semicolon_delimited.csv"
    test_file.write_text("col1;col2\n5;6\n7;8\n9;10")  # 3 rows, valid structure

    df = load_csv_with_fallback(str(test_file), delimiters=["|", ";"])

    assert list(df.columns) == ["col1", "col2"]
    assert len(df) == 3


# Test 2: All delimiter attempts fail
def test_load_csv_all_delimiters_fail(tmp_path):
    test_file = tmp_path / "bad_delimiters.csv"
    test_file.write_text("not,structured,correctly")

    with pytest.raises(ValueError):
        load_csv_with_fallback(str(test_file))


# Test 3: Empty file should raise ValueError
def test_load_csv_empty_file(tmp_path):
    test_file = tmp_path / "empty.csv"
    test_file.write_text("")

    with pytest.raises(ValueError):
        load_csv_with_fallback(str(test_file))