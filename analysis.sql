-- SQLite dialect. Load data/sample.csv into the records table.
SELECT genre, COUNT(*) AS sessions, ROUND(SUM(watch_minutes)/60.0,2) AS watch_hours, ROUND(100.0*AVG(completed),2) AS completion_pct FROM records GROUP BY genre;
SELECT device, COUNT(DISTINCT user_id) AS viewers, SUM(watch_minutes) AS watch_minutes FROM records GROUP BY device;
