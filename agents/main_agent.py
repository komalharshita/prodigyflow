
"""
Main Agent for ProdigyFlow
-----------------------------------
This agent coordinates:
1. Cleaning Agent
2. Analysis Agent
3. Visualization Agent

It loads the raw dataset, cleans it, analyzes it,
and generates visualizations — all in one pipeline.
"""

import json
from pathlib import Path

# Importing your agents
from cleaning_agent import load_data, clean_dataset, save_data, get_cleaning_plan
from analysis_agent import analyze
from visualization_agent import create_visualizations


# ---------------------------------------------------------
# MAIN PIPELINE FUNCTION
# ---------------------------------------------------------
def run_pipeline(
    raw_csv_path="data/data_science_student_marks.csv",
    cleaned_csv_path="data/cleaned_student_data.csv"
):
    print("\n🚀 Starting ProdigyFlow Pipeline...\n")

    # -----------------------------------------------------
    # 1. LOAD RAW DATA
    # -----------------------------------------------------
    df = load_data(raw_csv_path)
    if df is None:
        print("❌ Unable to load dataset. Stopping pipeline.")
        return

    print("\n📌 Raw dataset loaded successfully.")
    print(df.head())

    # -----------------------------------------------------
    # 2. GENERATE CLEANING PLAN (Gemini-powered)
    # -----------------------------------------------------
    print("\n🧹 Generating cleaning plan...")
    plan = get_cleaning_plan(df.head().to_string(), "Automatically clean this dataset.")
    print(f"✨ Cleaning Plan: {plan}")

    # -----------------------------------------------------
    # 3. APPLY CLEANING STEPS
    # -----------------------------------------------------
    print("\n🔧 Applying cleaning steps...")
    cleaned_df = clean_dataset(df, plan)

    # Save cleaned dataset
    save_data(cleaned_df, cleaned_csv_path)
    print(f"📁 Cleaned dataset saved to: {cleaned_csv_path}")

    # -----------------------------------------------------
    # 4. ANALYSIS AGENT
    # -----------------------------------------------------
    print("\n📊 Running data analysis...\n")
    insights, metadata = analyze(cleaned_csv_path)

    print("=== INSIGHTS ===")
    print(json.dumps(insights, indent=2))

    print("\n=== METADATA ===")
    print(json.dumps(metadata, indent=2))

    # -----------------------------------------------------
    # 5. VISUALIZATION AGENT
    # -----------------------------------------------------
    print("\n📈 Generating visualizations...\n")
    vis_result = create_visualizations(cleaned_csv_path)

    print("=== VISUALIZATION SUMMARY ===")
    print(json.dumps(vis_result, indent=2))

    print("\n🎉 Pipeline completed successfully!\n")


# ---------------------------------------------------------
# ENTRY POINT
# ---------------------------------------------------------
if __name__ == "__main__":
    run_pipeline()
