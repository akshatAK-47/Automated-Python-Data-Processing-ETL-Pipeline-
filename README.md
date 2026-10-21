# Automated Python Data Processing & ETL Pipeline

A modular Python-based ETL (Extract, Transform, Load) pipeline that automates tabular data ingestion, cleaning, validation, SQLite database loading, and summary report generation using Python, Pandas, NumPy, and SQL.

## Project Overview

Data analysts frequently work with raw datasets containing duplicate records, missing values, inconsistent column names, incorrect data types, and invalid values. Cleaning these datasets manually can be repetitive, time-consuming, and error-prone.

This project provides a reusable pipeline that processes CSV and JSON files, applies configurable data-quality rules, separates valid and rejected records, stores cleaned data in a SQLite database, and generates structured reports for further analysis.

**Project type:** Data Engineering / Data Analytics  
**Primary language:** Python  
**Database:** SQLite  
**Core libraries:** Pandas, NumPy, pytest  
**Python version:** Python 3.10+  
**Project status:** Portfolio project — see the implementation and test results in this repository.

## Business Problem

Manual data preparation creates several challenges:

- Inconsistent data formats across input files.
- Duplicate records that can distort business metrics.
- Missing or invalid values that affect analytical accuracy.
- Repeated data-cleaning tasks.
- Limited traceability when records are rejected.
- Time-consuming preparation of reports for business analysis.

### Project Objectives

1. Automate the ingestion of CSV and JSON datasets.
2. Standardize column names and normalize appropriate text fields.
3. Identify duplicates, missing values, invalid records, and data-quality issues.
4. Preserve rejected records with reasons for rejection.
5. Load valid records into a local SQLite database.
6. Generate reusable data-quality and business summary reports.
7. Make the workflow reproducible, modular, and testable.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Pipeline logic, automation, and error handling |
| Pandas | Tabular data ingestion, transformation, and analysis |
| NumPy | Missing-value handling and numerical operations |
| SQLite | Local relational database storage |
| SQL | Data retrieval, aggregation, and business summaries |
| JSON | Structured input and report formats |
| pytest | Automated testing |
| Git and GitHub | Version control and project collaboration |

## Dataset and Data Source

This project is designed around an employee dataset with tabular fields such as:

| Column | Description |
|---|---|
| employee_id | Unique employee identifier |
| name | Employee name |
| department | Department or business function |
| age | Employee age |
| salary | Annual salary represented as a numeric value |
| joining_date | Employee joining date |

**Dataset source:** The repository's sample CSV and JSON files should be treated as synthetic demonstration data unless a real public dataset and its original source are explicitly documented here.

If you use synthetic records, they are generated for demonstrating data processing and are not real employee information.

For a real dataset, document its original URL, publisher, license, permitted uses, and any modifications. Do not describe synthetic data as a Kaggle or public GitHub dataset.

## ETL Architecture

The pipeline follows a modular Extract–Transform–Load workflow.

```text
               Raw CSV / JSON
                      |
                      v
                1. EXTRACT
          Read and inspect input data
                      |
                      v
               2. TRANSFORM
       Standardize columns and values
       Normalize text and data types
                      |
                      v
                3. VALIDATE
       Check required fields and rules
              /               \
             v                 v
       Valid Records      Rejected Records
             |                 |
             v                 v
         4. LOAD         Rejection Report
      SQLite Database
             |
             v
         5. REPORT
     Data Quality Metrics
     Business Summary CSV
     Cleaned CSV and JSON
```

### Processing Stages

**1. Extract**

- Read CSV files using Pandas.
- Read JSON files using a supported JSON structure.
- Handle file access errors, empty files, and malformed input.
- Preserve the original raw files.

**2. Transform**

- Standardize column names.
- Normalize applicable text fields.
- Convert numeric and date columns.
- Identify duplicate records.
- Apply documented missing-value rules.

**3. Validate**

- Check required columns and identifiers.
- Detect invalid numeric values, such as negative salaries.
- Identify missing required fields and invalid dates.
- Separate valid and rejected records.
- Record rejection reasons and data-quality statistics.

**4. Load**

- Create the SQLite database and required tables.
- Insert valid records using parameterized SQL operations.
- Apply database constraints and duplicate-load prevention.
- Use transaction handling to protect data integrity.

**5. Report**

- Export cleaned data.
- Save rejected records for investigation.
- Generate data-quality statistics.
- Produce summary reports using relevant business metrics.

## Repository Structure

```text
automated-python-etl-pipeline/
│
├── data/
│   ├── raw/
│   │   ├── employees.csv
│   │   └── employees.json
│   └── sample/
│       └── README.md
│
├── output/
│   └── .gitkeep
│
├── database/
│   └── .gitkeep
│
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── validate.py
│   ├── database.py
│   ├── reporting.py
│   └── pipeline.py
│
├── tests/
│   ├── __init__.py
│   └── test_pipeline.py
│
├── main.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Installation and Setup

### Prerequisites

- Python 3.10 or later.
- Git (optional for local execution, required for Git-based version control).
- A terminal such as PowerShell, Command Prompt, or Bash.

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/automated-python-etl-pipeline.git
cd automated-python-etl-pipeline
```
### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, use Command Prompt instead:

```cmd
.venv\Scripts\activate.bat
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The `requirements.txt` file should list the dependencies actually imported by the implementation, such as Pandas, NumPy, and pytest.

SQLite is included with Python's standard library in typical installations, so a separate SQLite server is not required.

## Running the Pipeline

Execute commands from the repository root.

### Process a CSV file

```bash
python main.py --input data/raw/employees.csv --format csv
```

### Process a JSON file

```bash
python main.py --input data/raw/employees.json --format json
```

The JSON command assumes the file follows the record structure supported by the implementation.

### Expected workflow

When execution completes successfully, the pipeline should:

1. Read the selected input file.
2. Standardize and transform its records.
3. Validate records and identify data-quality issues.
4. Separate accepted and rejected records.
5. Load accepted records into SQLite.
6. Generate the configured output files.

The actual command-line options and output paths must match the arguments implemented in `main.py` and `src/pipeline.py`.

## Data Cleaning and Validation Rules

The following rules describe the intended processing behavior. Confirm the exact rules against the implementation before treating them as guaranteed features.

| Data-quality issue | Intended handling |
|---|---|
| Inconsistent column names | Convert names to a consistent format |
| Extra whitespace | Trim applicable text fields |
| Missing optional values | Apply documented rules without inventing information |
| Missing required identifier | Reject the affected record |
| Duplicate identifier | Apply the configured deduplication policy and track affected records |
| Negative salary | Reject the record when salary is required and invalid |
| Invalid date | Flag or reject according to the validation policy |
| Incorrect numeric type | Convert where safe; otherwise flag or reject |
| Malformed input file | Report a clear error and stop the affected run |

**Data integrity principle:** Raw input files should remain unchanged. Rejected records should be retained in a separate output with sufficient information to investigate why they failed validation.

Deduplication rules should be documented explicitly. For example, keeping the first record for a repeated `employee_id` is a policy decision, not a universally correct rule.

## Output Files

A successful pipeline run is intended to generate the following artifacts.

| Output | Purpose |
|---|---|
| `output/cleaned_data.csv` | Validated records in CSV format |
| `output/cleaned_data.json` | Validated records in JSON format |
| `output/rejected_records.csv` | Rejected records and rejection reasons |
| `output/data_quality_report.json` | Record counts and data-quality statistics |
| `output/summary_report.csv` | Aggregated business metrics |

The exact filenames and output directory depend on the implementation configuration.

### Example data-quality report

The following is an illustrative structure, not measured output from an actual run.

```json
{
  "input_records": 100,
  "valid_records": 92,
  "rejected_records": 8,
  "duplicate_records": 3,
  "database_records_loaded": 92
}
```

These numbers are examples only. Actual values must be calculated from the input data and execution results.

### Example business summary

For an employee dataset, the summary could include:

- Employee count by department.
- Average salary by department.
- Total salary by department.
- Overall valid and rejected record counts.

These metrics should only appear if they are supported by the actual input schema and report implementation.

## SQLite Database Integration

SQLite provides a lightweight relational database for local development and portfolio demonstrations.

The intended database workflow includes:

1. Creating the database and table schema.
2. Defining a suitable primary key.
3. Loading cleaned records using parameterized SQL.
4. Preventing duplicate loads according to the chosen key policy.
5. Committing successful transactions and rolling back failed ones.
6. Querying the database to generate summary metrics.

### Example SQL queries

The following examples assume the database contains an `employees` table with the specified columns.

**1. Count employee records**

```sql
SELECT COUNT(*) AS employee_count
FROM employees;
```

**2. Count employees by department**

```sql
SELECT
    department,
    COUNT(*) AS employee_count
FROM employees
GROUP BY department
ORDER BY employee_count DESC;
```

**3. Calculate average salary by department**

```sql
SELECT
    department,
    ROUND(AVG(salary), 2) AS average_salary
FROM employees
GROUP BY department
ORDER BY average_salary DESC;
```

**4. Find employees with missing values**

```sql
SELECT *
FROM employees
WHERE employee_id IS NULL
   OR department IS NULL;
```

The fourth query is useful only if the schema permits such rows; a correctly enforced required identifier constraint should prevent null identifiers from entering the accepted-record table.

### Future database support

The project uses SQLite to avoid external server setup. A future version could support PostgreSQL or MySQL by replacing the connection layer, adapting SQL syntax where needed, and using a suitable database driver and configuration system.

## Testing

Automated tests should verify the pipeline's behavior without overwriting project data.

Run the test suite:

```bash
python -m pytest -v
```

The intended test coverage includes:

- Successful CSV ingestion.
- Successful JSON ingestion.
- Missing input files.
- Malformed JSON.
- Duplicate record handling.
- Missing values and invalid records.
- SQLite database loading.
- Report generation.
- End-to-end pipeline execution.

Tests should use temporary files and isolated test databases wherever appropriate.

**Testing status:** Run the command above and review the actual test results before describing the project as fully tested.

## Error Handling and Logging

The implementation should use Python's `logging` module to provide useful execution messages and error details.

Important practices include:

- Catching expected exceptions at appropriate boundaries.
- Using context managers for file and database resources.
- Reporting invalid input clearly.
- Using parameterized SQL rather than constructing queries from raw values.
- Avoiding silent exception handling.
- Creating output directories when required.
- Avoiding partially written reports where practical.

These practices make the pipeline easier to troubleshoot and maintain.

## Performance Measurement

Automation may reduce repetitive data-cleaning effort, but the improvement must be measured rather than assumed.

A valid performance comparison should:

1. Define the baseline manual or unautomated workflow.
2. Use the same dataset and comparable cleaning rules.
3. Measure the baseline and automated workflow under documented conditions.
4. Repeat measurements where practical.
5. Calculate the improvement from recorded timings.

The percentage reduction can be calculated as:

\[
\text{Reduction (\%)} =
\frac{\text{Baseline Time} - \text{Automated Time}}
{\text{Baseline Time}} \times 100
\]

For example, a reduction from 50 minutes to 30 minutes would equal 40%. These are illustrative values, not results from this project.

Until you have valid measurements, do not claim that the project reduced manual cleaning time by 40%.

## Limitations

- The initial implementation is designed for local execution rather than distributed processing.
- SQLite is appropriate for a small portfolio project but is not a substitute for every production database.
- Data-cleaning rules depend on the selected dataset and business requirements.
- Synthetic sample data cannot demonstrate performance on every real-world dataset.
- Runtime and data-quality results depend on input size, data structure, and system configuration.
- The project does not automatically guarantee that every accepted record is correct for every business use case.

## Future Improvements

Potential extensions include:

- Support for additional CSV and JSON schemas.
- PostgreSQL and MySQL connectivity.
- Configurable validation rules.
- Structured logging to a file.
- A reproducible performance benchmark.
- More comprehensive unit and integration tests.
- Automated CI testing with GitHub Actions.
- Dashboard integration with Power BI.
- Scheduled data ingestion and incremental processing.
- Improved data-quality metrics and visualizations.

## Skills Demonstrated

This project is intended to demonstrate practical knowledge of:

- Python programming and modular code organization.
- Pandas-based data processing.
- NumPy numerical operations.
- CSV and JSON file handling.
- Data cleaning and validation.
- Exception handling and logging.
- SQLite database integration.
- SQL queries and aggregations.
- Automated testing with pytest.
- Git and GitHub version control.
- ETL workflow design and reporting.

## License

The repository's code license and the dataset's license are separate considerations.

Include a `LICENSE` file only after choosing a license appropriate for your code and confirming that the dataset's terms permit the intended use. If the sample data is synthetic, document that fact clearly.

A code license does not grant rights to third-party datasets.


No screenshots are claimed to be available in this README.

## Author

**Akshat Jain**

B.Tech in Computer Science and Engineering

Areas of interest: Data Analytics, Python Automation, SQL, Data Engineering, and Business Reporting.

GitHub: https://github.com/akshatAK-47


---

*This is a portfolio project intended for learning and demonstration. Feature descriptions, performance claims, and test status should be verified against the actual implementation and execution results.*
