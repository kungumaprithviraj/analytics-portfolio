from pathlib import Path
import csv, sqlite3, json
base=Path(__file__).parent
with (base/'data/sample.csv').open() as f:
    reader=csv.reader(f); columns=next(reader); rows=list(reader)
connection=sqlite3.connect(':memory:')
numeric=['age', 'tenure_years', 'monthly_salary_inr']
connection.execute('CREATE TABLE records (' + ','.join('"'+c+'" '+('REAL' if c in numeric else 'TEXT') for c in columns)+')')
connection.executemany('INSERT INTO records VALUES ('+','.join('?' for _ in columns)+')',rows)
assert connection.execute('SELECT COUNT(*) FROM records').fetchone()[0] == 800
assert len({row[0] for row in rows}) == len(rows), 'Duplicate primary key'
for col in numeric:
    assert all(float(row[columns.index(col)]) >= 0 for row in rows), col
results=[]
for query in (base/'sql/analysis.sql').read_text().split(';'):
    if query.strip():
        cursor=connection.execute(query)
        results.append([dict(zip([d[0] for d in cursor.description], row)) for row in cursor.fetchall()])
(base/'reports/sql_results.json').write_text(json.dumps(results,indent=2))
print(f'Validated {len(rows)} rows; executed {len(results)} analysis queries.')
