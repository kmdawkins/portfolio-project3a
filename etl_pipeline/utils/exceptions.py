# =====================================================================
# File: exceptions.py
# Purpose: Define custom exceptions for clearer ETL error handling
# Author: Katherina Dawkins (Project 3A - Python ETL)
# Version: v1.0.0
# =====================================================================

class ETLError(Exception):
    """Base class for all ETL-related exceptions."""
    pass


class FileNotFoundErrorCustom(ETLError):
    """Raised when a required input file is missing."""
    def __init__(self, path):
        super().__init__(f"❌ File not found at path: {path}")


class InvalidFileExtensionError(ETLError):
    """Raised when the file extension is not allowed."""
    def __init__(self, path, allowed_extensions):
        super().__init__(f"❌ Invalid file extension for {path}. Allowed: {allowed_extensions}")


class CSVLoadError(ETLError):
    """Raised when CSV loading fails across all fallback delimiters."""
    def __init__(self, path):
        super().__init__(f"❌ Failed to load CSV from {path}. All delimiter attempts failed.")


class ColumnValidationError(ETLError):
    """Raised when required columns are missing from the DataFrame."""
    def __init__(self, missing_columns):
        super().__init__(f"❌ Missing required columns: {missing_columns}")
