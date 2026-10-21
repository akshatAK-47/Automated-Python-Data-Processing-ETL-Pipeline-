# Automated Python Data Processing & ETL Pipeline

A beginner-friendly portfolio project that reads CSV/JSON records, standardizes and validates them with Pandas/NumPy, loads valid rows into SQLite, and creates repeatable reports.

> **Data note:** Included records are synthetic examples created for testing. They are not a public employee dataset and do not represent real people.

## Business problem
Repeated manual preparation can introduce inconsistent columns, duplicate records, invalid values, and inconsistent reporting. This project demonstrates a reusable process for handling those issues.

## Workflow
`CSV/JSON → Extract → Transform → Validate → SQLite → Reports`

- **Extract:** read CSV or JSON input.
- **Transform:** standardize column names/text and parse numeric/date fields.
- **Validate:** separate valid rows from rejected rows and record reasons.
- **Load:** store valid records in SQLite.
- **Report:** create cleaned files, a quality JSON report, and a department summary.

## Structure
```text
automated-python-etl-pipeline/
├── data/raw/              # Synthetic CSV and JSON examples
├── data/sample/
├── output/                # Generated reports (ignored by Git)
├── database/              # Generated SQLite DB (ignored by Git)
├── src/
├── tests/
├── main.py
├── requirements.txt
└── README.md
```

## Requirements
Python 3.10+ and pip.

## Installation (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run
CSV:
```bash
python main.py --input data/raw/employees.csv --format csv
```
JSON:
```bash
python main.py --input data/raw/employees.json --format json --db database/json_etl.db --output-dir output/json
```

## Generated reports
- `cleaned_data.csv` and `cleaned_data.json`
- `rejected_records.csv` with rejection reasons
- `data_quality_report.json` with row counts and missing-value metrics
- `summary_report.csv` with employee count and average salary by department

## Validation rules
The example schema expects `employee_id`, `name`, `department`, `salary`, and `joining_date`. Rows with duplicate/missing IDs, missing or invalid required values, invalid dates, or negative salary values are rejected. The first occurrence of a duplicated ID is retained. Raw inputs are not modified.

## Example SQL
```sql
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department
ORDER BY employee_count DESC;
```

```sql
SELECT employee_id, name, salary
FROM employees
WHERE salary >= 60000
ORDER BY salary DESC;
```

## Tests
```bash
pytest -q
```

Tests cover CSV extraction, malformed JSON, duplicate/invalid validation, SQLite loading, summary queries, and an end-to-end pipeline.

## Performance claim
This repository does **not** claim a measured 40% time reduction. To use that figure on a resume, measure a documented baseline and the automated workflow on the same dataset, and report the percentage only when supported by comparable results.

## Limitations and future work
- Validation rules are tailored to the sample employee schema.
- Sample data is synthetic.
- Future improvements could add configurable schemas, stronger monitoring, larger-dataset benchmarks, and PostgreSQL/MySQL adapters.

## License
Project code is provided under the MIT License. If you replace the sample data with a third-party dataset, follow its license and attribution requirements.
