SQL 30-Day Challenge — Health Insurance Analytics
Structured SQL study focused on health insurance fraud detection and claims analytics.
Built around a self-designed textbook using the Israeli problem-first learning model.
Every problem is domain-specific — no generic retail or Titanic datasets.
What This Is
A 30-day daily SQL practice log. 2 hours per day. Pure MySQL.
Domain: Health insurance — claims data, fraud detection, loss ratio, TPA operations.
Tool: MySQL Workbench
Schema: Health insurance claims (members, policies, claims, providers)
This is the practice repo. The capstone project repo is here:
→ health-insurance-fraud-detection

Schema
Chapters 1–3 use a flat denormalised table — claims_flat — that mirrors
a typical TPA data export.
Chapters 4–12 use a normalised schema:
members    → member_id, member_name, age, city, gender, policy_start_date
policies   → policy_id, member_id, plan_type, sum_insured, premium_amount, status
claims     → claim_id, member_id, provider_id, claim_date, claim_amount,
             diagnosis_code, procedure_code, claim_status
providers  → provider_id, provider_name, city, provider_type
Setup script: schema/create_tables.sql

Progress
ChapterTopicStatusDate1SELECT✅ DoneDay 22WHERE✅ DoneDay 43Aggregations✅ DoneDay 64GROUP BY and HAVING🔄 In progressDay 85JOINs⬜ Not started—6Subqueries⬜ Not started—7CTEs⬜ Not started—8Window Functions⬜ Not started—9CASE WHEN⬜ Not started—10Date Functions⬜ Not started—11Data Cleaning⬜ Not started—12Advanced Fraud Queries⬜ Not started—
Folder Structure
sql-30day-challenge/
│
├── README.md
├── schema/
│   └── create_tables.sql
└── chapters/
    ├── ch01_select.sql
    ├── ch02_where.sql
    ├── ch03_aggregations.sql
    └── ...

Domain Context
Health insurance claims data involves four parties:
members, providers, TPAs, and insurers. Fraud patterns
this study covers:

Inception fraud — claims filed suspiciously close to policy start date
Duplicate billing — same claim submitted more than once
Round number billing — amounts divisible by 50,000 suggesting estimation
Provider churning — claim volumes exceeding physical facility capacity
Threshold manipulation — claims clustering just below review thresholds


Key Concepts by Chapter
Chapters 1–3 — Core querying: SELECT, WHERE, aggregations.
First fraud signal spotted: duplicate claim for member M101 in Chapter 1 P7.
Chapters 4–5 — GROUP BY, HAVING, JOINs.
First provider benchmark query: flagging providers above 1.4x average claim amount.
Chapters 6–7 — Subqueries and CTEs.
First auditable multi-step fraud detection logic.
Chapter 8 — Window functions.
LAG-based consecutive claim gap detection — the most interview-relevant query in the textbook.
Chapters 9–10 — CASE WHEN scoring, date functions.
Composite fraud risk tier and Indian financial year quarterly reporting.
Chapters 11–12 — Data cleaning and advanced fraud queries.
Full data quality audit query and production-grade composite fraud score.
