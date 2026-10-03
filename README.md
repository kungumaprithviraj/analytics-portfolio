# Netflix-style Streaming Analytics
**Author:** Kunguma Prithviraj Manmadhan  
**Stack:** Python · SQLite · Streamlit · Power BI measures

## Business question
Which genres and devices generate viewing activity and completed sessions?

## Run locally
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python analyze.py
streamlit run app.py
```
Run commands from this project folder. SQL analysis uses only the Python standard library.

## Deliverables
- `3,000` synthetic records in `data/sample.csv`
- Filterable dashboard with KPI cards, breakdown, table and CSV export
- Two executable SQLite analysis queries and generated results
- Power BI measures and a report build guide

## Data dictionary
| Column | Definition |
|---|---|
| `session_id` | session id |
| `user_id` | user id |
| `title` | title |
| `genre` | genre |
| `country` | country |
| `device` | device |
| `session_date` | session date |
| `watch_minutes` | watch minutes |
| `duration_minutes` | duration minutes |
| `completed` | completed |

## Interpretation and limits
Netflix-style project with invented titles and simulated sessions; not Netflix internal data. Completion means at least 90% of runtime. No subscription billing data, so revenue and subscriber churn cannot be inferred.

All data is fictional, generated with seed 42 for a learning portfolio. Findings demonstrate analysis methods and are not claims about a real employer, Netflix, or a retailer. Read `reports/sql_results.json` for computed results; do not present simulated outcomes as professional work achievements.
