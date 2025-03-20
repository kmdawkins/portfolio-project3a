-- ==========================================================
-- Script: 20250319_v1.0_create_etl_schema.sql
-- Purpose: Create a dedicated schema for ETL processing
-- Author: Katherina Dawkins (Project 3A - Python ETL)
-- Version: v1.0
-- ==========================================================

-- Drop schema if it already exists (CAUTION: Will delete all related objects)
DROP SCHEMA IF EXISTS etl CASCADE;

-- Create new ETL schema
CREATE SCHEMA etl;

-- Verify creation
COMMENT ON SCHEMA etl IS 'Schema for ETL processing, includes raw, staging, and transformed layers';