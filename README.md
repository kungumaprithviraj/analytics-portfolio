# Black Friday Sales Reporting
**Author:** Kunguma Prithviraj Manmadhan  
**Stack:** Python · SQLite · Streamlit · Power BI measures

## Business question
Which categories and regions contribute revenue and profit during the sales event?

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
- `2,500` synthetic records in `data/sample.csv`
- Filterable dashboard with KPI cards, breakdown, table and CSV export
- Two executable SQLite analysis queries and generated results
- Power BI measures and a report build guide

## Data dictionary
| Column | Definition |
|---|---|
| `order_id` | order id |
| `customer_id` | customer id |
| `order_date` | order date |
| `category` | category |
| `region` | region |
| `units` | units |
| `unit_price_inr` | unit price inr (INR) |
| `discount_pct` | discount pct |
| `revenue_inr` | revenue inr (INR) |
| `cost_inr` | cost inr (INR) |
| `profit_inr` | profit inr (INR) |

## Interpretation and limits
One row represents one single-category order. Revenue is after discount; profit is revenue minus simulated product cost, excluding tax, shipping, and overhead. No prior-year baseline is available.

All data is fictional, generated with seed 42 for a learning portfolio. Findings demonstrate analysis methods and are not claims about a real employer, Netflix, or a retailer. Read `reports/sql_results.json` for computed results; do not present simulated outcomes as professional work achievements.
