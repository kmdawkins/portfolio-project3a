# Git Commit Message Log - Project 3A (ETL Workflow)


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
