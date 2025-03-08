# Git Commit Message Log - Project 3A (ETL Workflow)

## chore(.gitignore): refine exclusions for PostgreSQL ETL workflow
- Removed SQLite references (Project 3A exclusively uses PostgreSQL)
- Ignored Python cache files in etl_pipeline/utils/ (except db_connector.py)
- Strengthened security by emphasizing .env should not be committed
- Removed unnecessary Airflow metadata tracking
- Ensured tracking for etl_pipeline/jobs/ (formerly scripts/)