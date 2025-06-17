import pandas as pd
from fuzzywuzzy import process
import os

VALID_COUNTRIES = [
    "India", "United States", "United Kingdom", "Canada", "Australia",
    "Germany", "France", "Spain", "China", "Japan"
]

def standardize_email(email):
    if pd.isnull(email) or '@' not in str(email):
        return None
    return str(email).strip().lower()

def correct_country(country):
    if pd.isnull(country):
        return None
    match, score = process.extractOne(str(country), VALID_COUNTRIES)
    return match if score >= 80 else None

def correct_data(df):
    log = []
    
    # Fix emails
    for idx, email in df['Email'].items():
        new_email = standardize_email(email)
        if new_email != email:
            log.append((idx, 'Email', f"{email} → {new_email}"))
            df.at[idx, 'Email'] = new_email

    # Fix country names
    for idx, country in df['Country'].items():
        corrected = correct_country(country)
        if corrected != country:
            log.append((idx, 'Country', f"{country} → {corrected}"))
            df.at[idx, 'Country'] = corrected

    # Remove duplicates
    before = len(df)
    df = df.drop_duplicates().reset_index(drop=True)
    after = len(df)
    if before != after:
        log.append(('ALL', 'Duplicate Removal', f"Removed {before - after} duplicate rows"))

    return df, log

def log_corrections(log_path, log_entries):
    with open(log_path, 'w', encoding='utf-8') as f:
        for entry in log_entries:
            f.write(f"Row {entry[0]} | Column: {entry[1]} | Fix: {entry[2]}\n")
    print(f"Corrections logged to {log_path}")

def run_correction_agent(input_df, log_file):
    corrected_df, corrections_log = correct_data(input_df)
    log_corrections(log_file, corrections_log)
    return corrected_df

# For standalone run
if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)
    df = pd.read_csv("input/messy_customers.csv")
    cleaned_df = run_correction_agent(df, "logs/correction_log.txt")
    cleaned_df.to_csv("output/cleaned_after_correction.csv", index=False)
