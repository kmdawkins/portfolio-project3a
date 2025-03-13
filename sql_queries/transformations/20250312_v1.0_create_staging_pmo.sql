-- =================================================
-- Script: create_staging_pmo.sql
-- Purpose: Create staging table for raw PMO data ingestion
-- Author: Katherina Dawkins (Project 3A - Python ETL)
-- =================================================

-- Drop table if it exists to avoid duplication errors.
DROP TABLE IF EXISTS staging_pmo;

-- Create staging table (without constraints or indexes)
CREATE TABLE staging_pmo (
    payment_no              VARCHAR(20),
    transaction_date        DATE,
    campaign_id             VARCHAR(10),
    description             TEXT,
    contract_no             VARCHAR(20),
    purchase_order          VARCHAR(20),
    purchase_requisition    VARCHAR(20),
    project_no              VARCHAR(50),
    payment_entity          VARCHAR(50),
    amount_usd              NUMERIC(15,2),
    amount_cny              NUMERIC(15,2)
);