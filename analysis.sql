-- SQLite dialect. Load data/sample.csv into the records table.
SELECT department, COUNT(*) AS employees, ROUND(100.0*SUM(CASE WHEN attrition='Yes' THEN 1 ELSE 0 END)/COUNT(*),2) AS snapshot_attrition_pct, ROUND(AVG(monthly_salary_inr),2) AS avg_salary FROM records GROUP BY department;
SELECT overtime, COUNT(*) AS employees, ROUND(100.0*SUM(CASE WHEN attrition='Yes' THEN 1 ELSE 0 END)/COUNT(*),2) AS snapshot_attrition_pct FROM records GROUP BY overtime;
