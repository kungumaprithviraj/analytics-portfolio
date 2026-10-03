-- SQLite dialect. Load data/sample.csv into the records table.
SELECT category, ROUND(SUM(revenue_inr),2) AS revenue, ROUND(SUM(profit_inr),2) AS profit, ROUND(100.0*SUM(profit_inr)/NULLIF(SUM(revenue_inr),0),2) AS margin_pct FROM records GROUP BY category;
SELECT order_date, COUNT(*) AS orders, ROUND(SUM(revenue_inr),2) AS revenue, ROUND(AVG(revenue_inr),2) AS average_order_value FROM records GROUP BY order_date;
