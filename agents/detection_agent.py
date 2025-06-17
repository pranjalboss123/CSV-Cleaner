# agents/detection_agent.py

import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import os

VALID_COUNTRIES = [
    "India", "United States", "United Kingdom", "Canada", "Australia",
    "Germany", "France", "Spain", "China", "Japan"
]

def load_data(file_path):
    return pd.read_csv(file_path)

def detect_missing_fields(df):
    issues = []
    for index, row in df.iterrows():
        if pd.isnull(row['Email']) or '@' not in str(row['Email']):
            issues.append((index, 'Email', 'Missing or malformed email'))
        if pd.isnull(row['Name']) or len(str(row['Name']).strip()) == 0:
            issues.append((index, 'Name', 'Missing name'))
    return issues

def detect_duplicates(df):
    duplicates = df[df.duplicated()]
    return duplicates.index.tolist()

def detect_invalid_countries(df):
    issues = []
    for index, country in enumerate(df['Country']):
        if pd.isnull(country) or process.extractOne(str(country), VALID_COUNTRIES)[1] < 80:
            issues.append((index, 'Country', f'Invalid country: {country}'))
    return issues

def log_issues(log_path, issues):
    with open(log_path, 'w', encoding='utf-8') as f:
        for issue in issues:
            f.write(f"Row {issue[0]} | Column: {issue[1]} | Issue: {issue[2]}\n")
    print(f"Issues logged to {log_path}")

def run_detection_agent(input_file, log_file):
    df = load_data(input_file)
    issues = []
    issues.extend(detect_missing_fields(df))
    issues.extend([(i, 'ALL', 'Duplicate row') for i in detect_duplicates(df)])
    issues.extend(detect_invalid_countries(df))
    log_issues(log_file, issues)
    return df, issues

# For direct run
if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)
    run_detection_agent("input/messy_customers.csv", "logs/detection_log.txt")
