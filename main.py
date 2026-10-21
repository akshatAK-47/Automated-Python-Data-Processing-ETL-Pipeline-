import argparse
import json
import logging
from src.pipeline import run_pipeline

def main():
    parser = argparse.ArgumentParser(description="Automated Python Data Processing & ETL Pipeline")
    parser.add_argument("--input", required=True, help="Path to CSV or JSON input")
    parser.add_argument("--format", choices=["csv", "json"], default=None)
    parser.add_argument("--output-dir", default="output")
    parser.add_argument("--db", default="database/etl.db")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
    try:
        print(json.dumps(run_pipeline(args.input, args.format, args.output_dir, args.db), indent=2))
    except (FileNotFoundError, ValueError, OSError) as exc:
        logging.error("Pipeline failed: %s", exc)
        raise SystemExit(1) from exc

if __name__ == "__main__":
    main()
