# ProcessAutomation
Automating using Python. Organizing files, merging information from multiple APIs. Scheduling. 

This repository contains a modular automation framework that can:

Organize and process files from various sources

Merge and transform data from multiple APIs

Generate reports

Run scheduled tasks

Maintain detailed logs for debugging and auditability

Support automated testing with pytest

The goal is to provide a scalable foundation for building end‑to‑end automations that can be extended for personal workflows, business processes, or freelance client projects.


Structure

ProcessAutomation/
│
├── data/               # Input data, downloaded files, or API responses
├── logs/               # Runtime logs for debugging and audit trails
├── reports/            # Generated reports (CSV, JSON, summaries)
├── scheduler/          # Scheduling scripts (cron-like automation)
├── tests/              # Pytest-based automated tests
├── utils/              # Reusable helper modules (API calls, file ops, etc.)
├── workingimages/      # Temporary or processed images (if used)
│
├── .gitignore          # Git ignore rules
├── .python-version     # Python version pinning
└── README.md           # Project documentation


features :
1. File Automation
Automatically organizes files into structured folders

Cleans, renames, or transforms files as needed

2. Multi‑API Integration
Fetches data from multiple APIs

Merges and normalizes responses

Handles errors and retries gracefully

3. Scheduling
Runs tasks on a schedule (daily, hourly, etc.)

Uses Python‑based schedulers or OS‑level cron

4. Logging
Centralized logs stored in /logs

Useful for debugging and long‑running automations

5. Reporting
Generates summary reports

Saves outputs to /reports

6. Testing
pytest tests stored in /tests

Ensures reliability and prevents regressions

🛠️ Tech Stack
Python 3.x

Requests / httpx for API calls

Pandas for data merging (if used)

Schedule / APScheduler for automation

Pytest for testing

Logging module for structured logs

how to run 

git clone https://github.com/quest2know/ProcessAutomation.git
cd ProcessAutomation

python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

install required extensions 

python main.py
