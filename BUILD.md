# Build the Power BI report
1. Import `data/sample.csv` with Get Data → Text/CSV; name the table `records`.
2. Set identifiers and categories to Text; numeric measures to Whole/Decimal Number; dates to Date where present.
3. Add each measure from `measures.dax` separately using New measure. Format rates as percentages and INR measures as currency.
4. Create KPI cards from the measures, a bar chart by `genre`, a detail table, and category slicers. Add date and region/device/location slicers where available.
5. Validate totals against `reports/sql_results.json` and save your report as `netflix-streaming-analytics.pbix`.

A PBIX is not included; this folder contains a reproducible build guide and measures.
