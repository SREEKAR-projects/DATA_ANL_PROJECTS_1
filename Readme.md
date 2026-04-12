
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
