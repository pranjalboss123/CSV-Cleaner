import pandas as pd
import random
import os

# Sample names and countries (for fallback enrichment)
FAKE_NAMES = ['John Doe', 'Jane Smith', 'Alex Kumar', 'Sara Li', 'Raj Patel']
DEFAULT_COUNTRY = "India"

def enrich_data(df):
    log = []

    for idx, row in df.iterrows():
        # Enrich missing Name
        if pd.isnull(row['Name']) or str(row['Name']).strip() == '':
            new_name = random.choice(FAKE_NAMES)
            df.at[idx, 'Name'] = new_name
            log.append((idx, 'Name', f"Filled missing name → {new_name}"))

        # Enrich missing Country
        if pd.isnull(row['Country']) or str(row['Country']).strip() == '':
            df.at[idx, 'Country'] = DEFAULT_COUNTRY
            log.append((idx, 'Country', f"Filled missing country → {DEFAULT_COUNTRY}"))

    return df, log

def log_enrichment(log_path, log_entries):
    with open(log_path, 'w', encoding='utf-8') as f:
        for entry in log_entries:
            f.write(f"Row {entry[0]} | Column: {entry[1]} | Enrichment: {entry[2]}\n")
    print(f"Enrichment logged to {log_path}")

def run_enrichment_agent(input_df, log_file):
    enriched_df, enrichment_log = enrich_data(input_df)
    log_enrichment(log_file, enrichment_log)
    return enriched_df

# For standalone run
if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)
    df = pd.read_csv("output/cleaned_after_correction.csv")
    enriched_df = run_enrichment_agent(df, "logs/enrichment_log.txt")
    enriched_df.to_csv("output/final_cleaned_output.csv", index=False)
