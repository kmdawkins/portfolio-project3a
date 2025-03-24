import pytest
import pandas as pd
from io import StringIO
from etl_pipeline.utils.csv_loader import load_csv_with_fallback



# Test 1: Load succesffully with default comma delimiter
def test_load_csv_with_fallback_delimiter(tmp_path):
    test_file = tmp_path / "semicolon_delimited.csv"
    # First line is valid; second line triggers on_bad_lines="error"
    test_file.write_text("col1;col2\n5;6\n7")  # uneven row for bad delimiter

    # "|" will trigger bad line error, ";" should succeed
    df = load_csv_with_fallback(str(test_file), delimiters=["|", ";"])

    assert list(df.columns) == ["col1", "col2"]
    assert len(df) == 2



# Test 2: First delimiter fails, second one (semicolon) succeeds
def test_load_csv_with_fallback_delimiter(tmp_path):
    test_file = tmp_path / "semicolon_delimited.csv"
    # Make the first row clearly structured for semicolon
    test_file.write_text("col1;col2\n5;6\n7;8\n9;10")  # add more rows to trigger bad_lines


    # First delimiter will split nothing correctly, fallback ";" will work
    df = load_csv_with_fallback(str(test_file), delimiters=["|", ";"])

    assert list(df.columns) == ["col1", "col2"]
    assert len(df) == 2



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

    with pytest.raises(ValueError):
        load_csv_with_fallback(str(test_file))
