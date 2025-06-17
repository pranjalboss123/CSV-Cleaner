import os
import pandas as pd
from agents.detection_agent import run_detection_agent
from agents.correction_agent import run_correction_agent
from agents.enrichment_agent import run_enrichment_agent

# checks folders exist
os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)
os.makedirs("logs", exist_ok=True)

def run_full_pipeline(input_path):
    print(f"\n🚀 Running full agent pipeline on: {input_path}")

    # Step 1: Detection
    df, detection_issues = run_detection_agent(
        input_file=input_path,
        log_file="logs/detection_log.txt"
    )

    # Step 2: Correction
    df = run_correction_agent(
        input_df=df,
        log_file="logs/correction_log.txt"
    )

    # Step 3: Enrichment
    df = run_enrichment_agent(
        input_df=df,
        log_file="logs/enrichment_log.txt"
    )

    # Final output
    output_path = "output/final_cleaned_output.csv"
    df.to_csv(output_path, index=False)
    print(f"\n✅ Final cleaned CSV saved at: {output_path}")

if __name__ == "__main__":
    input_csv = "input/messy_customers.csv"
    if os.path.exists(input_csv):
        run_full_pipeline(input_csv)
    else:
        print(f"❌ No input file found at: {input_csv}")
