# agents/analysis_agent.py
"""
Analysis Agent for ProdigyFlow
-----------------------------------
Performs simple Exploratory Data Analysis (EDA):
- Loads the cleaned CSV
- Computes summary statistics
- Detects correlations
- Identifies missing values
- (Optional) Uses Google Gemini to generate a short insight summary

The goal is simplicity — easy to understand for students
and easy to debug during dry runs.
"""

import pandas as pd
import json
from pathlib import Path

# Optional: Gemini (Google AI Python SDK)
try:
    from google import genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False


# ---------------------------------------------------------
# Helper: Run Gemini to generate insights (safe fallback)
# ---------------------------------------------------------
def generate_gemini_summary(text: str) -> str:
    """
    Generates a short AI summary of the insights.
    If Gemini or the API key is missing, returns a fallback string.
    """
    if not GEMINI_AVAILABLE:
        return "Gemini summary unavailable (SDK not installed)."

    try:
        client = genai.Client()
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=f"Summarize these data insights in simple English:\n{text}"
        )
        return response.text
    except Exception:
        return "Gemini summary unavailable (API issue)."


# ---------------------------------------------------------
# MAIN ANALYSIS FUNCTION
# ---------------------------------------------------------
def analyze(cleaned_csv_path: str, logger=None):
    """
    Performs simple EDA.
    Returns:
        insights (dict)
        metadata (dict)
    """

    if logger:
        logger.info("Loading cleaned dataset...")
    df = pd.read_csv(cleaned_csv_path)

    # ---- Basic dataset info ----
    num_rows, num_cols = df.shape

    missing_count = df.isna().sum().to_dict()
    missing_percent = (df.isna().mean() * 100).round(2).to_dict()

    describe_stats = df.describe(include="all").to_dict()

    # ---- Correlation (only numeric columns) ----
    try:
        corr_matrix = df.corr(numeric_only=True).round(3).to_dict()
    except Exception:
        corr_matrix = {}

    # ---- Prepare insights ----
    insights = {
        "dataset_overview": {
            "rows": num_rows,
            "columns": num_cols,
            "column_names": list(df.columns),
        },
        "missing_values": {
            "count": missing_count,
            "percent": missing_percent,
        },
        "summary_statistics": describe_stats,
        "correlation_matrix": corr_matrix,
    }

    # ---- Add Gemini summary if possible ----
    gemini_input_text = json.dumps(insights, indent=2)
    gemini_summary = generate_gemini_summary(gemini_input_text)
    insights["ai_summary"] = gemini_summary

    # ---- Metadata for tracking ----
    metadata = {
        "status": "analysis_complete",
        "num_numeric_columns": len(df.select_dtypes(include="number").columns),
        "used_gemini": GEMINI_AVAILABLE,
    }

    if logger:
        logger.info("Analysis completed successfully.")

    return insights, metadata


# ---------------------------------------------------------
# Simple test run
# ---------------------------------------------------------
if __name__ == "__main__":
    # Example dry-run test
    print("Running a dry test of analysis_agent...\n")

    sample_path = "data\\data_science_student_marks.csv"
    sample_path = str(Path(sample_path).resolve())

    print("NOTE: This test will only work if a sample file exists.")
    print("File:", sample_path)

    try:
        insights, meta = analyze(sample_path)
        print("\nINSIGHTS:")
        print(json.dumps(insights, indent=2))
        print("\nMETADATA:")
        print(meta)
    except FileNotFoundError:
        print("Sample file not found. Dry run complete (no crash).")
