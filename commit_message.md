# Git Commit Message Log - Project 3A (ETL Workflow)

## [2025-03-13] Initial Python Script for Loading Staging Table

**Commit:** `feat: create initial Python script for loading pmo staging table`

**Reason:**  
- Other: New feature or functionality

**Details (Optional):**  
- First draft of `load_staging_pmo.py` to automate bulk loading of transaction data into `staging_pmo` table.
- Script currently focuses on reading CSV and inserting data using psycopg2.
- Will add error handling, logging, and validation in subsequent iterations.

**Files Affected:**
- `etl_pipeline/jobs/load_staging_pmo.py`


## [2025-03-12] Apply SemVer create_staging_pmo.sql

**Commit:** `docs: update commit_messages.md to align with mini-template for SemVer change log`

**Reason:**  
- Other: Applied SemVer naming for version control and future pipeline automation.

**Details (Optional):**  
- Renamed 'create_staging_pmo.sql` to `20250312_v1.0_create_staging_pmo.sql` for consistent version tracking as part of schema creation history.
- Ensures alignment with SemVer patterns used in Project 2A and prepares for automated ETL workflows.

**Files Affected:**
- `sql_queries/transformations/20250312_v1.0_create_staging_pmo.sql`



## [2025-03-12] Fix create_staging_pmo.sql Script

**Commit:** `fix: correct error in staging_pmo.sql script`

**Reason:**  
- Other: Corrected invalid schema reference causing script failure

**Details (Optional):**  
- Corrected table name reference by removing the `staging.` schema prefix since no "staging" schema exists in the database.
- Updated script to create table as `staging_pmo` without schema reference.
- Verified fix successfully via psql: script runs and creates intended table.

**Files Affected:**
- `sql_queries/transformations/create_staging_pmo.sql`


## [2025-03-12] commit_message.md Update

**Commit:** `chore: update commit_message.md with template`

**Reason:**  
- Personal working files or notes (e.g., developer notes, temp scripts)


**Details (Optional):**  
- Template added to maintain documentation consistency
- Internal documentation for ongoing learning and process clarification.
- Not relevant for production or sharing-will revisit if standardizing team documentation.

## chore: add commit_messages.md to track commit history  

- Created commit_messages.md in the project root  
- Documented commit details for better version tracking  
- Ensured consistent Git commit messaging for Project 3A  


## chore(.gitignore): refine exclusions for PostgreSQL ETL workflow
- Removed SQLite references (Project 3A exclusively uses PostgreSQL)
- Ignored Python cache files in etl_pipeline/utils/ (except db_connector.py)
- Strengthened security by emphasizing .env should not be committed
- Removed unnecessary Airflow metadata tracking
- Ensured tracking for etl_pipeline/jobs/ (formerly scripts/)

### Template

## [YYYY-MM-DD] .gitignore Update

**Commit:** `chore: update .gitignore to exclude <file_or_pattern_name>`

**Reason:**  
- [ ] Sensitive information (e.g., credentials, secrets)
- [ ] Large or auto-generated files not needed in repo (e.g., logs, backups, datasets)
- [ ] Personal working files or notes (e.g., developer notes, temp scripts)
- [ ] Other: _(brief explanation if different)_

**Details (Optional):**  
- <Add any specific details or future reminders, e.g., "Revisit if shared workflow requires it.">

**Files Affected:**
- `relative/file/path/goes_here.sql`
- `relative/file/path/goes_here.py`
