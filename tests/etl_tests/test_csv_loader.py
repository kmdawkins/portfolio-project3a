import pytest
import pandas as pd
from io import StringIO
from etl_pipeline.utils.csv_loader import load_csv_with_fallback



# Test 1: Load succesffully with default comma delimiter
def test_load_csv_with_default_delimiter(tmp_path):
    test_file = tmp_path / "valid_comma.csv"
    test_file.write_text("col1,col2\n1,2\n3,4")


    df = load_csv_with_fallback(str(test_file))
    assert not df.empty
    assert list(df.columns) == ["col1", "col2"]
    assert len(df) == 2


# Test 2: First delimiter fails, second one (semicolon) succeeds
def test_load_csv_with_fallback_delimiter(tmp_path):
    test_file = tmp_path / "semicolon_delimited.csv"
    test_file.write_text("col1;col2\n5;6\n7;8")

    df = load_csv_with_fallback(str(test_file), delimiters=[",", ";"])
    assert not df.empty
    assert "col1" in df.columns


# Test 3: All delimiter attempts fail
def test_load_csv_all_delimiters_fail(tmp_path):
    test_file = tmp_path / "bad_delimiters.csv"
    test_file.write_text("") # no readable structure (empty line)


    with pytest.raises(ValueError):
        load_csv_with_fallback(str(test_file))



# Test 4: Empty file should return empty DataFrame
def test_load_csv_empty_file(tmp_path):
    test_file = tmp_path / "empty.csv"
    test_file.write_text("")

    df = load_csv_with_fallback(str(test_file))
    assert isinstance(df, pd.DataFrame)
    assert df.empty