import os
import pytest
from etl_pipeline.utils.file_checker import check_file_exists, validate_file_extension


# Fixture to create a temporary test file
@pytest.fixture
def temp_test_file(tmp_path):
    temp_file = tmp_path / "example.csv"
    temp_file.write_text("test,data\n1,2")
    return str(temp_file)

# Test 1: File exists
def test_check_file_exists_valid(temp_test_file):
    assert check_file_exists(temp_test_file) is True

# Test 2: Files does not exist
def test_check_file_exists_invalid():
    assert check_file_exists("non_existent_file.csv") is False

# Test 3: Valid extension
def test_validate_file_extension_valid():
    asser_validate_file_extension("data.csv", [".csv", ".txt"]) is True

# Test 4: Invalid extension
def test_validate_file_extension_invalid():
    assert validate_file_extension("data.json", [".csv", ".txt"]) is False